#from newspaper import Article
#import re
import nltk
import operator
import csv
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import json
# left_wing, neutral, right_wing,
import newspaper
left_wing = [
    "https://act.tv/"
   # "https://www.newyorker.com/",
   # "http://www.theglobetoday.com/"
]
left_center = [

]
neutral = [

]
right_center = [

]
right_wing = [

]

ps = PorterStemmer()

keywords_csv = open("keywords.csv", "w")
keywords_file = open("keywords.txt", "w")

keywords_writer = csv.writer(keywords_csv, delimiter=',')
#affiliate, topic, frequecy
def gather(list_of_urls, affiliate):
    number_of_articles = 0
    for url in list_of_urls:
        keywords_list = {}
        nltk.download('punkt')
        site = newspaper.build(url, memoize_articles=False)
        for i in range(len(site.articles)):
            article = site.articles[i]
            try:
                article.download()
            except:
                continue
            try:
                article.parse()
            except:
                continue
            try:
                article.nlp()
            except:
                continue

            # add to the total number of articles scraped for this affiliation
            number_of_articles+=1

            # Add words to the dict or increase occurances
            for word in article.keywords:
                print(word +"\n")
                word = ps.stem(word)
                if word in keywords_list:
                    keywords_list[word] += 1
                    
                else:
                    keywords_list[word] = 1

            sorted_keywords = sorted(keywords_list.items(), key=operator.itemgetter(1))
            # backup
            if (i != 0):
                keywords_file.truncate()
            keywords_file.write(str(sorted_keywords))

            print("Article Done")
        #sorted_keywords = reversed(sorted(keywords_list.items(), key=operator.itemgetter(1)))




        #keywords_csv.close()
        print("end")

    # affiliate done, update csv
    for word, frequency in keywords_list.items():
        ratio = round(frequency/number_of_articles,3)
        keywords_writer.writerow([affiliate, word, str(ratio)])
    keywords_csv.close()
    print("CSV done")

gather(left_wing, "left_wing")


    # if i != 0 and i%20 == 0:
    #     #keywords_csv.truncate(0)
    #     sorted_authors = sorted(authors_list.items(), key=operator.itemgetter(1))
    #     sorted_category = sorted(category_list.items(), key=operator.itemgetter(1))
    #     sorted_keywords = sorted(keywords_list.items(), key=operator.itemgetter(1))
    #     #authors_csv.write(str(sorted_authors))
    #     #category_csv.write(str(sorted_category))
    #     keywords_csv.write(str(sorted_keywords))
    #
    #     # authors_csv = open("Authors.txt", "w")
    #     # category_csv = open("Categories.txt", "w")
    #     # keywords_csv = open("keywords.txt", "w")
    #     print("saved")

#regex = "([a-b]{1}[a-e]{1})"
#matches = re.findall(regex, text)
#print(matches)
#print(article.is_media_news())
#if article.is_media_news():
#    print("Do Stuff Here")


#print(article.nlp())

# ToDo: Collect quotes

# ToDo: Find sources (who said quotes and official citations)

# ToDo: Reverse Image search. If used a lot, less reliable

# ToDo: Check url


#cnn_paper = newspaper.build('http://cnn.com')
#print (text)
#for article in cnn_paper.articles:
#    article.download()
#    article.parse()
#    authors = article.authors

    # print(article.authors)

#get quotes (have citation?)
#get author