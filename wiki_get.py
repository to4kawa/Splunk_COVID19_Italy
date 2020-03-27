import requests
import pandas as pd
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Italy'
res = requests.get(url)
soup = BeautifulSoup(res.content, "lxml")
data=soup.find_all('table', {"wikitable mw-collapsible"})
df = pd.read_html(str(data), keep_default_na=False)[0]
df=df.iloc[:,0:28]
df.columns=['Date','VDA','LIG','PIE','LOM','VEN','TN','BZ','FVG','EMR','MAR','TOS','UMB','LAZ','ABR','MOL','CAM','BAS','PUG','CAL','SIC','SAR','ConfirmedNew','ConfirmedTotal','DeathsNew','DeathsTotal','ActiveICU','ActiveTotal']
daf=df[df['Date'].str.contains('^2020')]
daf.to_csv('Splunk_COVID19_Italy.csv', index=False)
