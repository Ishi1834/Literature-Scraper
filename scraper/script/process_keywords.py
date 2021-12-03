def keyword_analyser(summary,row, allKeywords, excellWriter):
    wordArr = summary.split()
    columnPosition = 6
    keywordRanking = 0
    for keyword in allKeywords:
        numberOfTimes = wordArr.count(keyword)
        excellWriter.write(row+1,columnPosition,numberOfTimes)
        keywordRanking = keywordRanking + numberOfTimes
        columnPosition = columnPosition + 1
    keywordRanking = round((keywordRanking / len(allKeywords)),2) 
    excellWriter.write(row+1, columnPosition-len(allKeywords)-1, keywordRanking)
    return keywordRanking
"""
keywordsarray will be given as the 3rd argument and replaced with allKeywords
"""