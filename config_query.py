bearer_token = ""

#query = "((#Bitcoin OR #BTC OR BTC OR #Bitcoin OR #HarmonyOne OR ETH OR #Ethereum OR DOT OR #Polkadot OR #cryptocurrency)(((#Ukraine OR #Russia)(war OR conflict OR crisis OR economy)) OR (#UkraineRussiaWar OR #RussiaUkraineWar))) lang:en -is:retweet"
query = "((#Bitcoin OR #BTC) (#Ukraine OR #Russia)) lang:en -is:retweet"
#fields=author_id,created_at,entities,geo,id,in_reply_to_user_id,possibly_sensitive,public_metrics

start_time = "2022-03-24T00:00:00Z"
end_time = "2022-03-2T00:00:00Z"

#end_time = "2022-03-25T06:00:00Z"

max_results = 100


#ukraine and (economy or cryptocurrency)
#ukraine and (war or conflict or crisis) 
#UkraineRussianWar
#russia and (economy or cryptocurrency)
#russia and (war or conflict or crisis) 
#usa and (war or conflict or crisis)
#emma watson or harry potter [Control Groups]
#cleanenergy	[Control Groups]
