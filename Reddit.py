"""
The Reddit API task 
"""
import requests
import pandas as pd



def run_reddit_etl():
    """
    Access Reddit API
    Data Transformation
    Data loading into the S3 bucket
    """

    #API connection
    CLIENT_ID = '##############'
    SECRET_KEY = '##############'
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID,SECRET_KEY)
    data = {
        'grant_type':'password',
        'username':'Fabulous_Ability9756',
        'password':'##############'
    }
    headers = {'User-Agent':'MyAPI/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers= headers)
    TOKEN = res.json()['access_token']
    headers['Authorization'] = f'bearer {TOKEN}'


    #Data ingestion
    res = requests.get('https://oauth.reddit.com/r/dataengineering/top/?t=day', headers= headers, params={'limit':100})

    #Data Wrangling and Transformation
    df = pd.DataFrame(columns= ['Title','Post','Upvotes','Upvote_ratio','Created_date','Link','User'] )
    p = res.json()['data']['children']
    today = pd.Timestamp.today().date()
    
    for post in p:
        ser = pd.Series({'Title':post['data']['title'],'Post':post['data']['selftext'],'Upvotes':post['data']['ups'],'Upvote_ratio':post['data']['upvote_ratio'],'Created_date':today,'Link':post['data']['url'],'User':post['data']['author']}, index = ['Title','Post','Upvotes','Upvote_ratio','Created_date','Link','User'])
        df.loc[len(df)] = ser


    #Data Loading after Transformation
    df.to_csv(f"s3://reddit-bucket-kb/Reddit{today}.csv")