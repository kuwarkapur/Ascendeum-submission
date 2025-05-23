import pandas as pd
df= pd.read_csv('/content/analysis_id (1)(in).csv')

df.info()

df.columns=[col.lower().strip() for col in df.columns]

bid_stat= df.groupby('bidder')[['response_count','prebid_win_count']].sum().reset_index()

bid_stat['win_rate']=bid_stat['prebid_win_count']/bid_stat['response_count']

bid_stat= bid_stat[bid_stat['response_count']>0]

bid_stat= bid_stat.sort_values(by='win_rate',ascending=False)

bid_stat.head()
