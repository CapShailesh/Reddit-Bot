#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:26:34 2020

@author: lenovo
"""

import praw
from PyDictionary import PyDictionary
import enchant

# create the objects from the imported modules

# reddit api login
reddit = praw.Reddit(client_id='KxOAB4O72F13yw',
                     client_secret='4oAfqabyhhZ5rHbkicmRUxANnQ4',
                     username='testbotsh',
                     password='testbotsh',
                     user_agent='testbot by /u/CapShailesh')

subreddit = reddit.subreddit('dankmemes')
keyphrase = '!link'

for comment in subreddit.stream.comments():
    if keyphrase in comment.body:
        submission = comment.submission
        try:
            comment.reply('[Enjoy]' + '(' + submission.url + ')');
            print('posted to ' + comment.author.name)
        except:
            print('to frequent' + comment.author.name + submission.url)
       # Output: the URL the submission points to
                         # or the submission's URL if it's a self post