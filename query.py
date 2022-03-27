import requests
import pandas as pd
import rfc3339
import iso8601
from datetime import timedelta

from config_query import *
from utils import *
from config import bearer_token


class TwitterQuery:
    def __init__(self,
                 end_point="https://api.twitter.com/2/tweets/search/recent"):
        self.end_point = end_point
        self.max_results = 100
        self.df = None

    def build_query(self,
                    query,
                    start_time,
                    end_time) -> dict:
        """
        build twitter api query with params

        :param query: query to perform
        :param start_time: start time of scrape
        :param end_time: max end time of scrape
        :return: dict of query
        """
        return {
            'query': query,
            'tweet.fields': 'created_at,author_id,entities,public_metrics',
            'user.fields': 'username',
            'max_results': self.max_results,
            'start_time': start_time.isoformat("T") + "Z",
            'end_time': end_time.isoformat("T") + "Z"
        }

    @staticmethod
    def get_header() -> dict:
        """
        Get the authorization data
        :return: dict
        """
        return {"Authorization": "Bearer {}".format(bearer_token)}

    def scrape_tweets(self,
                      query,
                      start_time,
                      duration_hours):
        """
        Get tweets for query from start_time for x hours
        :param query: query to make
        :param start_time: start time
        :param duration_hours: how many hours to scrape for
        :return: data file
        """
        entries = []
        for _ in range(duration_hours):
            response = requests.request("GET",
                                        self.end_point,
                                        headers=self.get_header(),
                                        params=self.build_query(query,
                                                                start_time,
                                                                start_time + timedelta(hours=30)))
            print(start_time)
            start_time += timedelta(minutes=30)

            try:
                for row in response.json()['data']:
                        entry = {"retweets": row["public_metrics"]["retweet_count"],
                                 "replies": row["public_metrics"]["reply_count"],
                                 "likes": row["public_metrics"]["like_count"],
                                 "quotes": row["public_metrics"]["quote_count"],
                                 "text": row["text"],
                                 "datetime": rfc3339.rfc3339(iso8601.parse_date(row["created_at"])),
                                 "place_id": 0}
                        if "contained_within" in row:
                            if "id" in row["contained_within"]:
                                entry["place_id"] = row["contained_within"]["id"]
                        entries.append(entry)
            except:
                print("No tweets returned")
        self.df = pd.DataFrame(data=entries)
        return self.df

    def save(self, prefix):
        self.df.to_csv("{0}.csv".format(prefix))


if __name__ == '__main__':
    query = "((#Bitcoin OR #BTC) (#Ukraine OR #Russia)) lang:en -is:retweet"
    start_time = datetime(2022, 3, 25)
    x = TwitterQuery()
    df = x.scrape_tweets(query, start_time, 3)
    print(df.head(35))
