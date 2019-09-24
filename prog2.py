import sqlite3
from sqlite3 import Error
import stream as twitter_stream
from time import strftime


stream = twitter_stream.create_stream()
tweet_buff, date_time, future = twitter_stream.get_stream(stream)

connection = sqlite3.connect("tweets.db")
tweet_db = connection.cursor()
tweet_db.execute('drop table if exists POPULAR_HASHTAG;')
tweet_db.execute('create table POPULAR_HASHTAG (tag_ID integer primary key autoincrement,hashtag text);')
connection.commit()
fp = open('report.txt', 'w')

for tweet in tweet_buff:
    if 'entities' in tweet:
        hashtags = tweet['entities']['hashtags']
        for hashtag in hashtags:
            tweet_db.execute('INSERT INTO POPULAR_HASHTAG (hashtag) VALUES (?);', [hashtag['text']])
            connection.commit()

result = tweet_db.execute('select hashtag, count(*) as count from POPULAR_HASHTAG group by hashtag order by count desc limit 10;')
popHashtags = result.fetchall()

print('{}\t{}'.format(date_time,future))
fp.write('{}\t{}\n'.format(date_time,future))
for popHashtag in popHashtags:
    print(popHashtag[0].encode('utf-8') + '\t{}'.format(popHashtag[1])) #encoding to  priduce hashtags in that are not in english
    fp.write(popHashtag[0].encode('utf-8') + '\t{}\n'.format(popHashtag[1]))

connection.close()