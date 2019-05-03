import csv

names = list()
names1 = list()
namesTemp = list()
with open('names.csv', 'r', encoding="utf-8") as names_file:
    csv_names = csv.reader(names_file)
    with open('names1.csv', 'r', encoding='utf-8') as temp_file:
        csv_temp = csv.reader(temp_file)
        for line in csv_names:
            names1.append(line[0])
        for lineTemp in csv_temp:
            namesTemp.append(lineTemp[0])


for name in names1:
    flag = True
    for nameTemp in namesTemp:
        if(name == nameTemp):
            flag = False
    if flag:
        names.append(name)

print(names)

with open('names.csv', 'w', encoding='utf-8') as data_file:
    csv_writer = csv.writer(data_file)
    for name in names:
        line = [name]
        csv_writer.writerow(line)

