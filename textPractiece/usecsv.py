import os,re,csv

def writecsv(filename, the_list):
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        a = csv.writer(f, delimiter=',')
        a.writerows(the_list)

def opencsv(filename):
    f=open(filename, 'r', encoding='utf8')
    reader=csv.reader(f)
    output=[]
    for i in reader:
        output.append(i)
    f.close()
    return output