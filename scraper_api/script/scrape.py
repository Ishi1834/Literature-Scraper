from script.make_soup import create_soup
from script.process_keywords import keyword_analyser

def scrape_articles(myLink, allKeywords, articlesMin, articleDict, checkIfIn, count):
    
    soup = create_soup(myLink)
    pageArticles = 0 #count how many articles are in each page

    for article in soup.find_all("div", class_="gs_r gs_or gs_scl"):
        
        # erros are bypassed using try and except
        try:
            title = article.h3.a.text
            description = article.find(class_="gs_rs").text
            link = article.h3.a.get('href') 
            prevCite = article.find("a", class_="gs_or_cit gs_or_btn gs_nph")
            cite = prevCite.find_next_sibling("a")
            otherArticles = cite.find_next_sibling("a")
            citations = cite.text
            citations = int(citations.split()[2]) # converts 'Cited by 1367' to 1367
            relatedArticles = "https://scholar.google.com" + otherArticles.get('href')
        except:
            continue

        if title in checkIfIn:
            continue

        #adds title to checkIfIn list
        checkIfIn.append(title)
        
        #using keyword_analyser() to see how many times a given keyword appears
        keywordRanking = keyword_analyser(description, allKeywords)
        
        #adding to dict
        articleDict[count] = {'title': title ,"description":description,"link":link,"citations":citations, "ranking": keywordRanking, 'relatedArticles': relatedArticles}
        
        pageArticles = pageArticles + 1
        count = count + 1
    """
        recursion is used to run the script again if the number of articles is less than minimum number given by the input
    """
    if len(articleDict) >= articlesMin:
        return articleDict
    else:
        try:
            newLink = articleDict.get(count-pageArticles)['relatedArticles'] 
            return scrape_articles( newLink, allKeywords, articlesMin, articleDict, checkIfIn, count) 
        except:
            newLink = articleDict.get(count)['relatedArticles'] 
            return scrape_articles( newLink, allKeywords, articlesMin, articleDict, checkIfIn, count) 




"""
articleReturn creates a dict to add information about each article
it is also used to check whether an article has already been added
"""
