import os
import glob
import pandas as pd

for x in glob.glob('????_powerhealth_??????.log'):
	timestr=(x[17:23])
	time_conv = pd.to_datetime(timestr,format='%d%m%y')
	df = pd.read_csv(x,index_col=False)
	df = df[~df.isin(["6553.5","16777215","nan","[unused]"]).any(axis=1)]
	df = df.rename(columns={' Ahc_daily': 'Ahc_daily'})
	df = df[df.Ahc_daily != 6553.5]
	df = df.sort_values(by=['hourmeter'], ascending=True)
	f = len(df.index) + 1
	timestamp = pd.date_range(time_conv, periods=f, freq='-1D', closed='right')[::-1]
	df.insert(0,'Time',timestamp,True)
	df.to_csv("{0}.csv".format(x), index=False)
