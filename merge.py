import csv

dataset1=[]
dataset2=[]

with open("scraped-final.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset1.append(row)

with open("scraped2.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset2.append(row)

headers1=dataset1[0]
star_data1=dataset1[1:]

headers2=dataset2[0]
star_data2=dataset2[1:]

headers=headers1+headers2

star_data=star_data1+star_data2

# for inx,data_row in enumerate(star_data1):
#     star_data.append(star_data1[inx]+star_data2[inx])

with open("scraped2-final.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)