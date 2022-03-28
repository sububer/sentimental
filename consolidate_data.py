import pandas as pd

df = pd.read_csv("data/2022323_infer.csv")
df_price = pd.read_csv("data/FTX_BTCUSD, 30.csv")

df['datetimeindex'] = pd.to_datetime(df['datetime'])


dftrain = pd.DataFrame()
dfprice_full = pd.DataFrame()
dftrain['joy_mean'] = df.resample('1H', on='datetimeindex').joy.mean()
dftrain['fear_mean'] = df.resample('1H', on='datetimeindex').fear.mean()
dftrain['surprise_mean'] = df.resample('1H', on='datetimeindex').surprise.mean()
dftrain['sadness_mean'] = df.resample('1H', on='datetimeindex').sadness.mean()
dftrain['others_mean'] = df.resample('1H', on='datetimeindex').others.mean()
dftrain['neu_mean'] = df.resample('1H', on='datetimeindex').neu.mean()
dftrain['neg_mean'] = df.resample('1H', on='datetimeindex').neg.mean()
dftrain['pos_mean'] = df.resample('1H', on='datetimeindex').pos.mean()
dftrain['quotes_mean'] = df.resample('1H', on='datetimeindex').quotes.mean()
dftrain['likes_mean'] = df.resample('1H', on='datetimeindex').likes.mean()
dftrain['replies_mean'] = df.resample('1H', on='datetimeindex').replies.mean()

dftrain['joy_std'] = df.resample('1H', on='datetimeindex').joy.std()
dftrain['fear_std'] = df.resample('1H', on='datetimeindex').fear.std()
dftrain['surprise_std'] = df.resample('1H', on='datetimeindex').surprise.std()
dftrain['sadness_std'] = df.resample('1H', on='datetimeindex').sadness.std()
dftrain['others_std'] = df.resample('1H', on='datetimeindex').others.std()
dftrain['neu_std'] = df.resample('1H', on='datetimeindex').neu.std()
dftrain['neg_std'] = df.resample('1H', on='datetimeindex').neg.std()
dftrain['pos_std'] = df.resample('1H', on='datetimeindex').pos.std()
dftrain['quotes_std'] = df.resample('1H', on='datetimeindex').quotes.std()
dftrain['likes_std'] = df.resample('1H', on='datetimeindex').likes.std()
dftrain['replies_std'] = df.resample('1H', on='datetimeindex').replies.std()


dfprice_full['pct'] = df_price.close.pct_change(periods=2)
dfprice_full['close'] = df_price.close
dfprice_full['datetimeindex'] = pd.to_datetime(df_price.time)

dataset = pd.merge_asof(dftrain, dfprice_full, on='datetimeindex')
dataset.to_csv("train_dataset.csv")
print(dataset.head())

if True:
    import matplotlib.pyplot as plt
    df_price.plot(x="time", y=["close"])
    fig, ax = plt.subplots(1, 1)
    dataset.plot(x='datetimeindex',y="pos_mean",yerr="pos_std",ax=ax,alpha=0.6,markersize=5,marker='o')
    dataset.plot(x='datetimeindex',y="neg_mean",yerr="neg_std",ax=ax,alpha=0.6,markersize=5,marker='o')
    plt.ylim([0, 0.5])

    df_price.plot("time", "close")

    plt.show()