#!/usr/bin/env python
# coding: utf-8
""" Compute word error rate """
wrong_prediction = 0
examples = 0
TargetList = []
HypList = []

with open("predictions.txt","r") as s:
    lines = s.readlines()
    for ln in lines:
        if ln.startswith("T-"):
            new_line = ln.rstrip("\n")
            TargetList.append(new_line.split("\t")[-1])
        elif ln.startswith("H-"):
            new_line = ln.rstrip("\n")
            HypList.append(new_line.split("\t")[-1])
            
for target, hypo in zip(TargetList, HypList):
    examples += 1
    if target != hypo:
        wrong_prediction += 1
        
    
WER = (wrong_prediction/examples)*100
print(f"WER:\t{WER}%")

#Output from spyder call 'get_cwd':
#WER:	22.22222222222222%

#Word rate error = 22.22%