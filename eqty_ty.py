#!/bin/python

import pandas as pd
from pathlib import PosixPath

#PATH = PosixPath('/home/alex/HDD/workshop/.datasets/KZnO/1.xls') 
PATH = '/home/alex/HDD/workshop/.datasets/KZnO/2.xls'

# read the format properly
df = pd.read_excel(PATH,verbose=True,sheet_name='данные')

