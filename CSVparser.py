# -*- coding: utf-8 -*-
"""###########################################################################################################
            This is a CSV parser that converts the commas (,) into blanck spaces ( )
#############################################################################################################"""

import csv
import time

print ("Welcome to the CSV parser")

answer = str(input("Has your data a header line (y/n)?"))

while answer !='y' and answer !='n':
    
    answer = str(input("Please enter 'y'(yes) or 'n' (no):"))
    
InputFile = str(input("Please enter the name of the input file (with extension):"))
OutputFile =str(input("Please enter the name of the output file (with extension):"))

start = time.time_ns()

if answer == 'y':
    
  """ HeaderSize = int(input("How many lines the header has?"))"""
    
  reader = csv.reader(open(InputFile, "r"), delimiter=',')
  writer = csv.writer(open(OutputFile, 'w', newline=''), delimiter=' ')
  writer.writerows(reader)
    
  with open (OutputFile, 'r+') as f: 
    
        lines=f.readlines()    
        f.seek(0)
        for i in lines:
            if i!=0:
                f.write(i)
        f.truncate()
              
elif answer == 'n':
    
 reader = csv.reader(open(InputFile, "r"), delimiter=',')
 writer = csv.writer(open(OutputFile, 'w', newline=''), delimiter=' ')
 writer.writerows(reader)
 
 end=time.time_ns()
    
 print ("The program has succesfully run in",end-start, "nanoseconds since the epoch")
    
  
    


