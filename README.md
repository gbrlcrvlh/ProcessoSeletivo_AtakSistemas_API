# 2ª Etapa do Processo Seletivo Atak Sistemas

**Problema Proposto:** 

>Desenvolver, em qualquer linguagem, uma API que faz uma pesquisa no google e devolve o resultado em json e/ou XML.
>Não utilizar as API do Google, como Search API.
>
>Deve se extrair do resultado do google:
>     Titulo
>    Link

**Solução Adotada:**

Foi desenvolvido uma API em Python capaz de fazer _web scrapping_ nas páginas de resultados de pesquisas no site do Google. A estrutura da API foi montada visando a expansão do projeto incluindo outras plataformas de pesquisas como Bing, Yahoo e etc.

Os dados podem ser obtidos através do endpoint `/googleSearch`, sendo apenas necessário passar os parâmetros `searchText` e `pagesNumber`

**Como inicializar a API:**

Deve-se certificar que as bibliotecas em python `flask`, `flask_restful`, `flask_cors` e `bs4` estejam devidamente instaladas na máqina. Desta forma, a API poderá ser inicializada através do seguinte comando:

```sh
python searchServer.py
```
Após a inicialização, a API poderá ser acessada através da porta 5000 do _localhost_
