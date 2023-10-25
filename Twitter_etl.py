import requests
import pandas as pd

CLIENT_ID = '################'
SECRET_KEY = '##########################'

auth = requests.auth.HTTPBasicAuth(CLIENT_ID,SECRET_KEY)

data = {
    'grant_type':'password',
    'username':'Fabulous_Ability9756',
    'password':'kbhattarai_de'
}

headers = {'User-Agent':'MyAPI/0.0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers= headers)

TOKEN = res.json()['access_token']

headers['Authorization'] = f'bearer {TOKEN}'

res = requests.get('https://oauth.reddit.com/r/dataengineering/top/?t=day', headers= headers, params={'limit':100})
df = pd.DataFrame(columns= ['Title','Post','Upvotes','Upvote_ratio','Created_date','Link','User'] )

p = res.json()['data']['children']
print(p)
today = pd.Timestamp.today().date()
for post in p:
    ser = pd.Series({'Title':post['data']['title'],'Post':post['data']['selftext'],'Upvotes':post['data']['ups'],'Upvote_ratio':post['data']['upvote_ratio'],'Created_date':today,'Link':post['data']['url'],'User':post['data']['author']}, index = ['Title','Post','Upvotes','Upvote_ratio','Created_date','Link','User'])
    df.loc[len(df)] = ser


df.to_csv(f"Reddit{today}.csv")
