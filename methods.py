import requests
from bs4 import BeautifulSoup as bs
import json

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'}

def get_loyal_token():
    resp = requests.get('https://www.andalusiahealth.com/',headers = headers)
    soup = bs(resp.content,'lxml')
    loyal_token = soup.find('script',{'data-id':'guide-client-id'})['data-value']
    return loyal_token
def get_data(location='andulasia'):
    loyal_token = get_loyal_token()
    headers = {
        'referer': 'https://www.andalusiahealth.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
        }

    params = {
        'address': location.lower(),
        'showProviderIndex': 'true',
        'disabledEmployedRankings': 'false',
    }

    response = requests.get(
        f'https://api.loyalhealth.com/search/{loyal_token}/3/1/search/all',
        params=params,
        headers=headers,
    )
    return response.json()

if __name__ == "__main__":
    print(get_data('andulasia'))