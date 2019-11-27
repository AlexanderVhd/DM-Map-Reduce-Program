import sys
import csv
import codecs
import re
import collections
import time

#set default encoding for all output in utf-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

#reduce function that returns top 20 most frequent words
def reduce(wordList):
    return wordList.most_common(20)

#map function that filters the stop words and maps the list words 
def mapWords(lst):
    filteredList = collections.Counter()

    stopWords = set(['an', 'a', 'at', 'be', 'for', 'do', 'its', 'such', 'have', 'all', 'your', 'of', 'most', 'off', 'is', 'http', 'am', 'me', 'or', 'so', 'who', 'as', 'from', 'him',
     'the', 'are', 'we', 'then', 'that', 'what', 'can', 'did', 'our', 'not', 'now', 'he', 'will', 'just', 'this', 'was', 'to', 'and', 'rt', 'you', 'on', 'with', 'has', 'i', 'if', 'in', 'my', 'by', 'it'])

    for word in lst:
        if word not in stopWords:
            filteredList.update({word:1})

    return filteredList


def readFile(filepath):
    tweetWords = []

    with open(filepath, newline='', encoding='utf-8') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')

        #get the column titles of the csv file
        header = next(readcsv)

        for row in readcsv:

            #remove links, words with special characters, and whitespace from line, then 
            tweet = re.sub(r"https:\S+|[!-@]\S+|[!-@$]|[_$]", "", row[2])
            tweet = tweet.strip()
            tweet = tweet.lower()
            words = tweet.split()
   
            #put words into a list
            for word in words:
                tweetWords.append(word)

    return tweetWords


def main():

    #read file 
    path = 'C:\\Users\\Taymoor\\Software Projects\\Project Data\\Donald-Tweets!.csv'
    wordList = readFile(path)

    #start timer
    startTime = time.clock()

    #map
    mapped = mapWords(wordList)

    #reduce 
    reduced = reduce(mapped)
    
    #end timer
    progTime = time.clock() - startTime


    print("\n\t\t\t\t\t\tSEQUENTIAL MAP REDUCE\n")
    print('Donald Trumps Top 20 Tweet Words by Frequency\n')

    #I assume you didn't want the frequency of every word in the file so I just gave the top 20 most frequent words in the file
    for wordFreq in reduced:
        print('%-*s: %4s' % (10, wordFreq[0], wordFreq[1]))
    
    #print time taken for program to complete
    #progTime = time.clock() - startTime
    print("\nTime Taken: %s seconds\n" % (progTime))
    


if __name__ == "__main__":
    main()

