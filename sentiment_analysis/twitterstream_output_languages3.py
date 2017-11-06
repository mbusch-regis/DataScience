import json
import pandas as pd
import matplotlib.pyplot as plt
import pylab


def readTwitterData(twitterDataFile):
    tweets = []
    with open(twitterDataFile, encoding="utf-8") as infile:
            for line in infile:
                    tweets.append(json.loads(json.loads(line)))
    print(type(tweets[0]))
    return tweets



if __name__ == '__main__':
    if sys.argv[1] == '':
        tweets_data_path = './req_output.json'
    

    tweets_data = []
    tweets = pd.DataFrame()
    tweets_data = readTwitterData('./req_output.json')


    tweets['tweet'] = list(map(lambda tweet: tweet['text'] if 'text' in tweet else None, tweets_data))
    tweets['lang'] = list(map(lambda tweet: tweet['user']['lang'] if 'user' in tweet else None, tweets_data))
    tweets_by_lang = tweets['lang'].value_counts()
    print (tweets_by_lang[:10]) #outputs top 10 languages

    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel('Languages', fontsize=15)
    ax.set_ylabel('Number of Tweets' , fontsize=15)
    ax.set_title('Top 10 Languages', fontsize=15, fontweight='bold')
    tweets_by_lang[:10].plot(ax=ax, kind='bar', color='green')

    pylab.show()
