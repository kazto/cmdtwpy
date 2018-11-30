#!/usr/bin/env python3

from requests_oauthlib import OAuth1Session
import sys
import os

CK = os.getenv('CMDTWPY_CONSUMER_KEY')
CS = os.getenv('CMDTWPY_CONSUMER_SECRET')
AT = os.getenv('CMDTWPY_ACCESS_TOKEN')
AS = os.getenv('CMDTWPY_ACCESS_TOKEN_SECRET')

if(not CK or not CS or not AT or not AS):
    print('please set environment variable:')
    print('  CMDTWPY_CONSUMER_KEY, CMDTWPY_CONSUMER_SECRET, CMDTWPY_ACCESS_TOKEN, CMDTWPY_ACCESS_TOKEN_SECRET')
    exit(1)

tw = OAuth1Session(CK, CS, AT, AS)

url = "https://api.twitter.com/1.1/statuses/update.json"

payload = ' '.join(sys.argv[1:])

res = tw.post(url, params = {"status": payload})

if res.status_code != 200:
    print("failed. %d" % res.status_code)

