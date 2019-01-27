#from newspaper import Article
#import re
import nltk
import operator
import csv
from nltk.stem import PorterStemmer
#from nltk.tokenize import sent_tokenize, word_tokenize
#import json
# left_wing, neutral, right_wing,
import newspaper
# left_wing = [
#    # "https://act.tv/"
#     "https://www.newyorker.com/",
#     "http://www.theglobetoday.com/",
#     "https://www.cnn.com/",
#     "https://www.huffingtonpost.com/",
#     "https://www.vox.com/",
#     "https://www.buzzfeed.com/",
#     "https://blacklivesmatter.com/",
#     "https://thinkprogress.org/",
#     "https://www.msnbc.com/",
#     "https://www.salon.com/",
#   #  "https://www.mediamatters.org/",
#     "https://abcnews.go.com/"
# ]

# right_wing = [
#     "https://www.therebel.media/",
#   #  "https://2ndvote.com/",
#     "https://www.breitbart.com/",
#    # "https://www.theblaze.com/",
#     "https://www.drudge.com/",
#     "https://www.foxnews.com/",
#     "https://dailycaller.com/",
#     "https://www.dailywire.com/",
#     "https://ijr.com/",
#     "https://www.lifezette.com/",
#     "https://www.thegatewaypundit.com/",
#     "https://www.newsmax.com/",
#     "https://pjmedia.com/",
#     "https://rsbnetwork.com/",
#     "http://thefederalist.com/",
#     "https://www.cnsnews.com/",
#     "https://freebeacon.com/",
#    # "https://townhall.com/",
#     #"https://twitchy.com/",
#     "http://www.freerepublic.com/home.htm",
#  #   "https://www.wnd.com/",
#   #  "https://www.infowars.com/"
# ]
center_left = [
    "https://www.msn.com/en-ca/news",
    "https://www.pbs.org/newshour/",
    "https://www.theverge.com/",
    "https://www.aljazeera.com/ ",
    "https://www.bbc.com/news/world",
    "https://www.cbsnews.com/",
    "https://www.cbc.ca/news",
    "https://www.ctvnews.ca/ ",
    "https://www.france24.com/en/",
    "https://www.latimes.com/"
]
neutral = [
    "https://www.c-span.org/",
    "https://ca.reuters.com/",
    "https://www.weforum.org/events/world-economic-forum-annual-meeting",
    "https://www.economist.com/",
    "http://www.pewresearch.org/",
    "https://www.euronews.com/",
    "https://www.dailyrecord.co.uk/"
]
center_right = [
    "https://nypost.com/",
    "https://nationalinterest.org/",
    "https://www.hoover.org/",
    "https://gulfnews.com/",
    "https://forbes.com",
    "https://calgarysun.com/",
    "https://www.bostonherald.com/",
    "https://www.dailynews.com/"
]
ps = PorterStemmer()

keywords_csv = open("keywords.csv", "w")
keywords_file = open("keywords.txt", "w")


#affiliate, topic, frequecy
def gather(list_of_urls, affiliate,file_name):
    csv_file = open(file_name + ".csv", "w")
    keywords_writer = csv.writer(csv_file, delimiter=',')
    number_of_articles = 0
    for url in list_of_urls:
        print(url)

        keywords_list = {}
        #nltk.download('punkt')
        site = newspaper.build(url, memoize_articles=False)

        last_title = ""
        for i in range(len(site.articles)):
            if i == 150:
                break
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

            if article.title == last_title:
                last_title = article.title
                continue
            last_title = article.title
            # add to the total number of articles scraped for this affiliation
            number_of_articles+=1

            # Add words to the dict or increase occurances
            for word in article.keywords:
                # print(word +"\n")
                word = ps.stem(word)
                if word in keywords_list:
                    keywords_list[word] += 1
                    
                else:
                    keywords_list[word] = 1

            sorted_keywords = sorted(keywords_list.items(), key=operator.itemgetter(1))

            # backup
            if (i != 0):
                keywords_file.truncate()
            #keywords_file.write(str(sorted_keywords))
            print(str(i) + ": " + article.title)
            #print("Article Done")
        #sorted_keywords = reversed(sorted(keywords_list.items(), key=operator.itemgetter(1)))




        #keywords_csv.close()
        print("end")

    count = 0
    print(affiliate)
    for i in reversed(sorted_keywords):
        if count == 30:
            break
        count += 1
        print (i)

    keywords_writer.writerow(["affiliation", "keyword", "ratio of articles that used this word"])
    print("# of articles \n")
    print(number_of_articles)
    # affiliate done, update csv
    for word, frequency in keywords_list.items():
        ratio = frequency/number_of_articles
        keywords_writer.writerow([affiliate, word, str(ratio)])
    csv_file.close()
    print("CSV done")
    return reversed(sorted_keywords)

#need to compare other side still.
def in_common(first, second):
    in_common = []
    for first_tuple in first:
        for second_tuple in second:
            if first_tuple[0] == second_tuple[0]:
                in_common.append(first_tuple)
    print(in_common)

# left_dict = gather(left_wing, "left_wing", "left")
# right_dict = gather(right_wing, "right_wing", "right")

center_left_dict = gather(center_left, "center_left", "center_left")
center_right_dict = gather(center_right, "center_right", "center_right")
neutral = gather(neutral, "neutral", "neutral")
#right_dict = gather(right_wing, "right_wing", "right")
# in_common(left_dict,right_dict)

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