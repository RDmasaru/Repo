#coding:utf-8

import os
import requests
import random

def bing_search(query):
    bing_url = ''
    MS_ACCTKEY = '3TlFTREHtLueRATpZTMxOQ4Fwa/oWNTGyh3Q4+VUBMs'

    payload = { '$format': 'json',
                'Query': "'"+query+"'",
              }
    r = requests.get(bing_url, params=payload, auth=('', MS_ACCTKEY))

    count = 0
    rand = random.randint(1,5)
    for item in r.json()['d']['results']:
        image_url = item['MediaUrl']
        root,ext = os.path.splitext(image_url)
        if ext.lower() == '.jpg':
            print image_url,
            r = requests.get(image_url)
            fname = "image.jpg"
            f = open(fname, 'wb')
            f.write(r.content)
            f.close()
            print "...save", fname
            count += 1
            if rand == count:
                break
