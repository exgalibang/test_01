import csv

file = 'C:\\Users\\hzluye\\Desktop\\info.csv'
data = csv.reader(open(file,'r'))

for user in data:
    username = user[0]
    password = user[1]
    print(username,password)
