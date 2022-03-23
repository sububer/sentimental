
import requests
import os
import json
import time

from config_query import *
from utils import *

endpoint = "https://api.twitter.com/2/tweets/search/recent"

params = {
    'query': query,
    'tweet.fields': 'created_at,author_id,entities,public_metrics',
    'user.fields': 'username'
}

#'expansions': 'author_id,referenced_tweets.id,geo.place_id,in_reply_to_user_id,referenced_tweets.id.author_id',

headers = {"Authorization": "Bearer {}".format(bearer_token)}

with open("dataset.jsonl", "w") as datafile:

    # MAKE FIRST REQUEST
    print("Getting tweets")
    response = requests.request("GET", endpoint, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    json_response = response.json()
    #datafile.write(json.dumps(json_response, indent=4, sort_keys=True))
    datafile.write(json.dumps(json_response))

    # PARSE PAGE
    try:
        
        for tweet_dict in json_response['data']:
            user_dict = json_response['includes']['users'] # read the dict with user data which comes separately from the tweet_dict
            
            # Add some user data to the tweet data dicty
            user_to_get = tweet_dict['author_id']
            
            for u in user_dict:
                if u['id'] == user_to_get:
                    tweet_dict['username'] = u['username']
                    tweet_dict['name'] = u['name']

            datafile.write(str(tweet_dict) + "\n")
    except:
        print("No tweets returned")

    # PAGINATE
    try:
        next_token = json_response['meta']['next_token'] # get next_token
        params['pagination_token'] = next_token # add pagination key to query dict
    except:
        print("No more pages")
    
    # KEEP GETTING PAGES
    while True:
            time.sleep(1)
            response = requests.request("GET", endpoint, headers=headers, params=params)
            if response.status_code != 200:
                raise Exception(response.status_code, response.text)
            json_response = response.json()
            try:          
                for tweet_dict in json_response['data']:
                    user_dict = json_response['includes']['users']
                    user_to_get = tweet_dict['author_id']
                    for u in user_dict:
                        if u['id'] == user_to_get:
                            tweet_dict['username'] = u['username']
                            tweet_dict['name'] = u['name']
                              
                datafile.write(str(tweet_dict) + "\n")
            
                next_token = json_response['meta']['next_token']
                params['pagination_token'] = next_token

            except:
                break
    
    print("Done")

    
# Converting json to dataframe
with open('dataset.jsonl', 'r') as f:
    json_list = json.load(f)
    list_series = []

# Convert each row to a series and append to the list
for row in json_list["data"]:
    list_series.append(pd.Series(row))

# Create Dataframe
df = pd.DataFrame(data=list_series)

# Clean dataframe
df= clean_df(df)


# Preprocess text data
preprocess_text(df)