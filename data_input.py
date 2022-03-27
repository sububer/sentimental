import datetime

from query import TwitterQuery

TQ = TwitterQuery()

# Essentially we look for crypto and a war related tweet
query = "((#Bitcoin OR #BTC OR BTC OR #Bitcoin OR #HarmonyOne OR ETH OR #Ethereum OR DOT OR #Polkadot OR #cryptocurrency)" \
        "(((#Ukraine OR #Russia)" \
        "(war OR conflict OR crisis OR economy))" \
        " OR (#UkraineRussiaWar OR #RussiaUkraineWar))) lang:en -is:retweet"

start_time = datetime.datetime.now() - datetime.timedelta(hours=24*6)
x = TwitterQuery()
x.scrape_tweets(query, start_time, 24*6*2)
x.save("{0}{1}{2}_{3}".format(
               start_time.year,
               start_time.month,
               start_time.minute,
               24*6))
