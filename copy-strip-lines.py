# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 01:00:02 2018

@author: Green
"""

import os
from pathlib import Path
import time


my_Path=Path("C:\\Users\\Green\\Desktop\\Python\\Time Series\\ITSM2000\\")
my_file_Path = Path("C:\\Users\\Green\\Desktop\\Python\\Time Series\\ITSM2000\\wine.tsm")
suffix=str(round(time.time()))
new_file_Path = Path("C:\\Users\\Green\\Desktop\\Python\\Time Series\\ITSM2000\\new_file"+suffix+".txt")
os.chdir(my_Path)

print(suffix)

print(my_file_Path.is_file())
print(new_file_Path.is_file())

if not new_file_Path.is_file():
    if my_file_Path.is_file():
        fp1=open("wine.tsm")
        with open("new_file"+suffix+".txt", 'w') as fp2:
            for line in fp1:
                fp2.write(line.strip()+'\n')
                
        fp1.close()