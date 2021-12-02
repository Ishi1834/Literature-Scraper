from make_soup import create_soup
from user_inputs import process_input
from make_spreadsheet import initiate_spreedsheet
from process_keywords import keyword_analyser

def scrape_articles(myLink):
    
    soup = create_soup(myLink)
    pageArticles = 0

    for article in soup.find_all("div", class_="gs_r gs_or gs_scl"):
        
        """
        Sometimes error occur for certain articles
        try and except is used so if a problem appears with an article it is skipped
        """
        try:
            title = article.h3.a.text
            description = article.find(class_="gs_rs").text
            link = article.h3.a.get('href')
            prevCite = article.find("a", class_="gs_or_cit gs_or_btn gs_nph")
            cite = prevCite.find_next_sibling("a")
            otherArticles = cite.find_next_sibling("a")
            citations = cite.text
            citations = int(citations.split()[2]) 
            relatedArticles = "https://scholar.google.com" + otherArticles.get('href')
        except:
            print('error with link', link)
            continue
        
        
        if title in checkIfIn:
            continue
        global count

        #using keyword_analyser() to see how many times a given keyword appears
        keywordRanking= keyword_analyser(description, count, keywordsArray, worksheet)

        worksheet.write(count+1,0,title)
        worksheet.write(count+1,1,description)
        worksheet.write(count+1,2,link)
        worksheet.write(count+1,3,citations)
        worksheet.write(count+1,4,relatedArticles)
        
        #adding to dict
        articleReturn[count] = {'title': title,"description":description,"link":link,"citations":citations, "ranking": keywordRanking, 'relatedArticles': relatedArticles}
        checkIfIn.append(title)

        count = count + 1
        pageArticles = pageArticles + 1
    """
        recursion is used to run the script again if the number of articles is less than minimum number given by the input
    """
    if len(articleReturn) >= minArticles:
        print('success')
    else:
        newLink = articleReturn[(count-pageArticles)]['relatedArticles']
        return scrape_articles(newLink)

articleReturn = {} 
checkIfIn = []
count = 0
url, keywordsArray, minArticles = process_input()
worksheet, workbook = initiate_spreedsheet(keywordsArray)
scrape_articles(url)
workbook.close()
print(count, 'Articles')