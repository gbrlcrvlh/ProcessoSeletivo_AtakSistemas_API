import requests
import bs4
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
from urllib.parse import urljoin

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

CONST_PARAM_SEARCH_TEXT = 'searchText'
CONST_PARAM_PAGES_NUMBER = 'pagesNumber'

def getGoogleSearchUrl(text):
    return 'https://www.google.de/search?q=' + text.replace(' ', '+')

def googleSearchScrapping(url, data, pagesNumber):
    base = "https://www.google.de"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }

    request_result=requests.get(url,headers=headers)
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")

    divs = soup.select('div.g')
    for div in divs:
        links = div.select("a")
        for link in links:
            title = link.select('h3')
            if len(title) >= 1:
                data.append({'title': title[0].get_text(), 'link': link['href']})

    next_page = soup.select_one("a#pnnext")
    if next_page and pagesNumber>0:
        next_page_link = urljoin(base,next_page.get("href"))
        return googleSearchScrapping(next_page_link, data, pagesNumber-1)

    return data

class googleSearch(Resource):
    def get(self):
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument(CONST_PARAM_SEARCH_TEXT, required=True)
        parser.add_argument(CONST_PARAM_PAGES_NUMBER, required=True)
        args = parser.parse_args()

        return {'data': googleSearchScrapping(getGoogleSearchUrl(args[CONST_PARAM_SEARCH_TEXT]), [], int(args[CONST_PARAM_PAGES_NUMBER])-1)}, 200
    pass

api.add_resource(googleSearch, '/googleSearch')

if __name__ == '__main__':
    app.run()
