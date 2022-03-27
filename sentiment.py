import pandas as pd
from pysentimiento import create_analyzer
from tqdm.auto import tqdm

analyzer = create_analyzer(task="sentiment", lang="en")
emotion_analyzer = create_analyzer(task="emotion", lang="en")

df = pd.read_csv('data/2022323_144.csv')

pos = []
neg = []
neu = []
fear = []
joy = []
others = []
sadness = []
surprise = []
for tweet in tqdm(df['text']):
    sent = analyzer.predict(tweet).probas
    feels = emotion_analyzer.predict(tweet).probas
    pos.append(sent['POS'])
    neg.append(sent['NEG'])
    neu.append(sent['NEU'])
    fear = feels["fear"]
    joy = feels["joy"]
    others = feels["others"]
    sadness = feels["sadness"]
    surprise = feels["surprise"]

df_infer = pd.DataFrame({'pos': pos,
                         'neg': neg,
                         'neu': neu,
                         'fear': fear,
                         'joy': joy,
                         'sadness': sadness,
                         'surprise': surprise,
                         'others': others})

result = pd.concat([df, df_infer], axis=1)
result.to_csv("{0}_infer.csv".format("2022323"))
