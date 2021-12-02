def process_input(title, keywords):
    title = title
    url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=' + title.replace(' ','+')
    if ( len(title) < 1 ) : url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=life+cycle+assessment+of+hydrogen+production+from+biomass+gasification'
    
    wordInput = keywords
    keywordsArray = wordInput.split()
    if ( len(wordInput) < 1 ) : keywordsArray = ['biomass', 'syngas', 'life cycle assessment', 'hydrogen', 'emissions', 'impacts', 'results', 'iso']

    numArticles = ''
    if ( len(numArticles) < 1 ) : numArticles = '20'
    
    return url, keywordsArray, int(numArticles)