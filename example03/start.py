#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# =============================================================================
__author__ = "Matthias Morath"
__copyright__ = "Copyright 2021"
__credits__ = ["Matthias Morath"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Matthias Morath"
__email__ = "matthias.morath@gmail.com"
__status__ = "Development"
# =============================================================================
from pydantic import BaseModel
from typing import List, Dict, Optional

"""
Your goal is to create a social media post model using pydantic. The model should have:
An author, which is a string
An optional co-author, which is a string
A date, which is a string
A title, which is a string
The content, which is a string
An ID, which is an integer
Likes, which is a list of strings

The post should also have a field for comments, which is a list of comment models. The model should have:
An author, which is a string
The comment, which is a string
Likes, which is an integer

Practice creating a social media post with whatever data you like, so long as it compiles.
"""

class Comment(BaseModel):
    author: str
    comment: str
    likes: int
    
class Post(BaseModel):
    author: str
    co_author: Optional[str] = None
    date: str
    title: str
    id: int
    likes: List[str]
    comments : List[Comment]

###############################################################################################################
# MAIN
###############################################################################################################
if __name__ == "__main__":
    
    comments = [
        Comment(author="johndoe", comment="This is a comment!",likes=2),
        Comment(author="johnPeter", comment="This is a shit!",likes=15)
        ]

    post = Post(
        author="johndoe",
        co_author="janedoe",
        date="1/1/1970",
        title="Cool post",
        content="Cool content",
        id=10101,
        likes=["johndoe","janedoe"],
        comments=comments
        )

    print(post)
    print(post.comments[0].author)