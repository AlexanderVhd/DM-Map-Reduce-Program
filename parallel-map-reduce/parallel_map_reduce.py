import sys
import csv
import codecs
import re
import functools
import collections
import time
import multiprocessing as mp

#set default encoding for all output in utf-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


#reduce function that updates the initial list 
def reduceList(mappedWords):
    wordFreqList = functools.reduce(reduceChunk, mappedWords)
    return wordFreqList.most_common(20)


#reduce function that updates the list with each chunk of words
def reduceChunk(reducedFreqList, chunkedList):
    reducedFreqList.update(chunkedList)
    return reducedFreqList


#mapping function to compute frequency of words in a chunk
def mapChunk(lst):
    mappedWords = collections.Counter()
    
    stopWords = set(['an', 'a', 'at', 'be', 'for', 'do', 'its', 'such', 'have', 'all', 'your', 'of', 'most', 'off', 'is', 'http', 'am', 'me', 'or', 'so', 'who', 'as', 'from', 'him',
     'the', 'are', 'we', 'then', 'that', 'what', 'can', 'did', 'our', 'not', 'now', 'he', 'will', 'just', 'this', 'was', 'to', 'and', 'rt', 'you', 'on', 'with', 'has', 'i', 'if', 'in', 'my', 'by', 'it'])

    for word in lst:
        if word not in stopWords:
            mappedWords.update({word:1})

    return mappedWords


#function that splits a list into chunks of n
def divideList(lst, n):
    for word in range(0, len(lst), n):
        yield lst[word:word + n]


#function to read twitter data from file
def readFile(filepath):
    tweetWords = []

    with open(filepath, newline='', encoding='utf-8') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')

        #get the column titles of the csv file
        header = next(readcsv)

        for row in readcsv:

            #remove links and words with special characters
            tweet = re.sub(r"https:\S+|[!-@]\S+|[!-@$]|[_$]", "", row[2])
            tweet = tweet.strip()   #remove whitespace from line
            tweet = tweet.lower()   #make all words lowercase for simplicity 
            words = tweet.split()   #split into words
   
            #put words into a list
            for word in words:
                tweetWords.append(word)

    return tweetWords


def main():
    
    resultFreq = collections.Counter()
    pool = mp.Pool(mp.cpu_count())

    #read file 
    path = 'C:\\Users\\Taymoor\\Software Projects\\Project Data\\Donald-Tweets!.csv'
    wordList = readFile(path)
    
    n = int(len(wordList) / mp.cpu_count())     #determine number of words each chunk will contain 
    chunkedList = list(divideList(wordList, n))     #split list into chunks

    #start timer
    startTime = time.clock()

    #map 
    mapped = pool.imap_unordered(mapChunk, chunkedList)
    pool.close()

    #reduce 
    topWordFreqs = reduceList(mapped)

    #end timer
    progTime = time.clock() - startTime  


    print("\n\t\t\t\t\t\tPARALLEL MAP REDUCE\n")
    print('Donald Trumps Top 20 Tweet Words by Frequency\n')

    ##I assume you didn't want the frequency of every word in the file so I just gave the top 20 most frequent words in the file
    for wordFreq in topWordFreqs:
        print('%-*s: %4s' % (10, wordFreq[0], wordFreq[1])) 

    #print time taken for program to complete
    print("\nTime Taken: %s seconds\n" % (progTime))
   


if __name__ == "__main__":
    main()
