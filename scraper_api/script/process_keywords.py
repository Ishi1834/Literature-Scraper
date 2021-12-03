def keyword_analyser(summary,allKeywords):
    wordArr = summary.split()
    keywordRanking = 0
    for keyword in allKeywords:
        numberOfTimes = wordArr.count(keyword)
        keywordRanking = keywordRanking + numberOfTimes
    keywordRanking = round((keywordRanking / len(allKeywords)),2) #changed 3 to len(allkeywords)
    return keywordRanking
"""
keywordsarray will be given as the 3rd argument and replaced with allKeywords
"""