from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
topic = "livetweet"

tweetFile = "C:/Codebase/TwitterSenti/Twitter-Sentiment-master/1Mtweets_en.txt"
with open(tweetFile, 'r',encoding="utf-8") as fp:
    line = fp.readline()
    cnt = 1
    while line:
        line = fp.readline()
        print(cnt)
        producer.send(topic,line.encode("utf-8"))
        cnt += 1


