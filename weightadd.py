#!/usr/bin/python
import sys
f=open('temp.txt','r')
results=f.readlines()
weight={}
cars=['A6L','ACCORD','COROLLA','BUICK','BYD','CRUZE','SATANA','FAW']
ratio={'whole':1100,'front':265,'back':367,'tire':392,'logo':1250}

for car in cars:
    weight[car] = .0

for i in range(len(results)/7):
    kind=results[7*i][:-1]
    for j in range(7*i+2, 7*i+7):
        line=results[j].split()
        weight[line[2][1:-1]] += float(line[0])*ratio[kind]

#sort weight
weight=sorted(weight.items(),key=lambda weight:weight[1], reverse=True)
print weight[0][0]
