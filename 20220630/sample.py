# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 20:09:54 2022

@author: mori
"""

result=[]
with open("data_org.txt") as f:
    for line in f:
        if line.isspace():
            continue
        line=line.strip()
        result.append(line)
        
with open("result.txt","w") as f:
    for line in result:
        f.write(line+"\n")
