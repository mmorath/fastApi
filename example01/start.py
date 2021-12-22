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

# use type hints
# remember type hints do not change anything they are hints
def add_integers(i:int,j:int):
    return i + j

###############################################################################################################
# MAIN
###############################################################################################################
if __name__ == "__main__":
    #import the variables
    print(add_integers(5,5))
