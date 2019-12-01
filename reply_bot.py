
# coding: utf-8

# In[1]:

import praw
import pdb
import re
import os
from praw.exceptions import APIException


# In[2]:

# creating a reddit instance
reddit = praw.Reddit('bot1')


# In[3]:

# text file to store posts that have already been replied to (later use a .csv or a sql database)
if not os.path.isfile('posts_replied_to.txt'):
    posts_replied_to = []
    
# loading the list of posts bot has already replied to
else:
    with open('posts_replied_to.txt', 'r') as f:
        posts_replied_to = f.read().split('\n')
        posts_replied_to = list(filter(None, posts_replied_to))


# In[5]:

# Get the top 5 values from our subreddit
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=10):
    #print(submission.title)
    
    # if we haven't replied to this post before
    if submission.id not in posts_replied_to:
        
        try:
            if re.search('i love python', submission.title, re.IGNORECASE):
                submission.reply('BOOM BOOM BOOM!')
                print('Bot Replying to ', submission.title)
        except APIException as e:
            print("Cannot reply to", submission.title, " because ", e)
        # Store that id into the list
        posts_replied_to.append(submission.id)


# In[6]:

# Write the updated list back to the text file
with open('posts_replied_to.txt', 'w') as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")