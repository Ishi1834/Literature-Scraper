<h1 align="center">Literature Scraper</h1>

<p align="center">A web scraper that gathers articles from google scholar and creates a ranking based on search keywords</p>

<h3 align="center">This repo contains 3 folders: </h3>
<p align="center">Scraper contains the python script which creates an excel document.</p>
<p align="center">Scraper_api contains the Flask api which returns a JSON object.</p>
<p align="center">Webpage contains the files for the deployed web page. </p>

A flask application is deployed on google cloud using the scraper_api
folder, when a user searches on the website a post request is sent 
To the flask application containing the title and keywords within a 
JSON object.
