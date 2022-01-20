
import csv
import pandas as pd

#put the file names in the 2 variables as below:-
file1 = ''
file2 = ''
# declare 2 empty lists d1 and d2

with open(file1,'r',encoding='utf8') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        d1.append(i)
        
with open(file2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        d2.append(i)
#pick header from d1[0] and put to h1 ref h2 and make it same for h1

h2 = d2[0]


#pick planet data from d1[1:] and assign to p_d1 refer to p_d2
p_d2 = d2[1:]
#add h1 and h2 and put in variable h


p_d =[]

for i in p_d1:
    p_d.append(i)
for j in p_d2:
    p_d.append(j)
with open("total_stars.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(p_d)
    
df = pd.read_csv('total_stars.csv')
df.tail(8)
