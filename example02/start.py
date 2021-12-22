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

class Comment(BaseModel):
    author: str
    
class User(BaseModel):
    username: str
    password: Optional[str] = None
    likes: Dict[str, int]
    comments: List[Comment]


class AdminUser(User):
    admin_password: str

###############################################################################################################
# MAIN
###############################################################################################################
if __name__ == "__main__":
    #import the variables
    pass 
