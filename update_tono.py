#!/usr/bin/env python
#-*- coding:utf-8 -*-

from tweepy.streaming import StreamListener, Stream
from tweepy.auth import OAuthHandler
from tweepy.api import API
import tweepy
import random
from search_image import bing_search

def get_oauth():
    # 以下4つのキー等は適宜取得して置き換えてください。
    consumer_key = ''
    consumer_secret = ''
    access_key = ''
    access_secret = ''
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    return auth

class AbstractedlyListener(StreamListener):
    def on_status(self, status):
      if not 'aaaaa' in status.author.screen_name:
        if not status.text.startswith(u'@' or u'＠' or u'RT'):
            if len(status.text) < 20 and len(status.text) != 1:
                if status.text.endswith(u'殿'):
                    if not '\n'  in status.text:
                        print status.author.screen_name
                        if status.text.endswith(u'殿様' or u'殿殿' or u'TONO'):
                            if status.text.endswith(u"殿様") and status.text.startswith(u"私の心は"):
                                api.create_favorite(status.id)
                                api.update_profile(name=status.text)
                                text = u"@" + status.author.screen_name + u" " + u"夏が過ぎ　風あざみ だれの憧れにさまよう 青空に残された" + status.text
                                search_text = status.text.encode('utf-8')
                                bing_search(search_text)
                                api.update_with_media(filename='./image.jpg',status=text, in_reply_to_status_id=status.id)

                            else:
                              if len(status.text) < 8:
                                api.create_favorite(status.id)
                                api.update_profile(name=status.text)
                                text = u"@" + status.author.screen_name + u" " + status.text + u"だYO! 🎶💃🎶"
                                search_text = status.text.encode('utf-8')
                                bing_search(search_text)
                                api.update_with_media(filename='./image.jpg',status=text, in_reply_to_status_id=status.id)

                        else:
                            rand = random.randint(1,6)
                            api.create_favorite(status.id)

                            if rand == 1:
                                api.update_profile(name=status.text)
                                text = u"@" + status.author.screen_name + u" " + status.text + u"だぞ"
                                search_text = status.text.encode('utf-8')
                                search_text = search_text.rstrip("殿")
                                bing_search(search_text)
                                api.update_with_media(filename='./image.jpg',status=text, in_reply_to_status_id=status.id)



                            elif rand == 2:
                                api.update_profile(name=status.text)
                                text = u"@" + status.author.screen_name + u" " + status.text + u"←これすきw"
                                search_text = status.text.encode('utf-8')
                                search_text = search_text.rstrip("殿")
                                bing_search(search_text)
                                api.update_with_media(filename='./image.jpg',status=text, in_reply_to_status_id=status.id)

                            elif rand == 3:
                                api.update_profile(name=status.text)
                                text = u"@" + status.author.screen_name + u" " + status.text + u"だゾウ🐘"
                                search_text = status.text.encode('utf-8')
                                search_text = search_text.rstrip("殿")
                                bing_search(search_text)
                                api.update_with_media(filename='./image.jpg',status=text, in_reply_to_status_id=status.id)

                            elif rand == 4:
                                api.update_profile(name=status.text)
                                text = u"@" + status.author.screen_name + u" " + status.text + u"ザマスw💁"
                                search_text = status.text.encode('utf-8')
                                search_text = search_text.rstrip("殿")
                                bing_search(search_text)
                                api.update_with_media(filename='./image.jpg',status=text, in_reply_to_status_id=status.id)

                            elif rand == 5:
                                api.update_profile(name=status.text)
                                text = u"@" + status.author.screen_name + u" " + status.text + u"かも"
                                search_text = status.text.encode('utf-8')
                                search_text = search_text.rstrip("殿")
                                bing_search(search_text)
                                api.update_with_media(filename='./image.jpg',status=text, in_reply_to_status_id=status.id)

                            else:
                                api.update_profile(name=status.text)
                                text = u"@" + status.author.screen_name + u" " + status.text + u"イェーイ"
                                search_text = status.text.encode('utf-8')
                                search_text = search_text.rstrip("殿")
                                bing_search(search_text)
                                api.update_with_media(filename='./image.jpg',status=text, in_reply_to_status_id=status.id)



if __name__ == '__main__':
    auth = get_oauth()
    api = tweepy.API(auth)
    stream = Stream(auth, AbstractedlyListener(), secure=True)
    stream.userstream()
