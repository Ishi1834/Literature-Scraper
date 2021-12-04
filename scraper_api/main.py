from flask import Flask, request
from flask_cors import CORS
from script.scrape import scrape_articles
from script.user_inputs import process_input


app = Flask(__name__)
CORS(app)

@app.route("/result", methods = ["POST","GET"])

def result():
    output = request.get_json()

    if len(output.keys()) < 2:
        return {"status":"BAD REQUEST"}

    #from here
    title = output['title']
    keywords = output['keywords']

    def run_script(title, keywords):

        count = 0
        articleReturn = {}
        checkIfIn = []         
        url, givenKeywords, minArticles = process_input(title, keywords)
        scrape_articles(url, givenKeywords, minArticles, articleReturn, checkIfIn, count)

        return(articleReturn)

    return run_script(title,keywords)
if __name__ == '__main__':
    app.run(debug=True,port=2000)