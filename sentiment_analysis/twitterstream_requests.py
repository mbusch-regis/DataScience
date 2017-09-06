import requests
from requests_oauthlib import OAuth1
import json

api_key = ''
api_secret = ''
access_token_key = ''
access_token_secret = ''

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(api_key, api_secret, access_token_key, access_token_secret)

r = requests.get(url, auth=auth)
print(r.status_code)

url = 'https://stream.twitter.com/1.1/statuses/sample.json'
r = requests.get(url, auth=auth, stream=True)
if r.encoding is None:
    r.encoding = 'utf-8'

with open('req_output.json', 'w') as ofile:
    for line in r.iter_lines(decode_unicode=True):
        if line:
            ofile.write(json.dumps(line))
            ofile.write('\n')
