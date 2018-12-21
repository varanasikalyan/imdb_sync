#-------------------------------------------------------------------------------
# Name:        __init__.py
# Purpose:
#
# Author:      kkrishnav
#
# Created:     15/10/2018
# Copyright:   (c) kkrishnav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from sqlalchemy import create_engine
import config

engine = create_engine(config.CONNECTION_STRING, echo=False)

from tsv_data import *