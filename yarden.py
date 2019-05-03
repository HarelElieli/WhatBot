import csv

names = list()
names1 = list()
with open('yarden2.csv', 'r', encoding="utf-8") as names_file:
    csv_names = csv.reader(names_file)
    for line in csv_names:
        names.append(line)

for name in names:
    try:
        if(name[0][0] == ' '):
            name = [name[0][1:], '+' + name[1]]
        if(name[0][-1] == ' '):
            name = [name[0][:-1], '+' + name[1]]
        names1.append(name)
    except:
        pass

with open('yarden3.csv', 'w', encoding='utf-8') as data_file:
    csv_writer = csv.writer(data_file)
    for name in names1:
        print(' '.join(name[0].split(' ')[-2:]))
        if(' '.join(name[0].split(' ')[-2:]) == 'אקסלים חדשות'):
            csv_writer.writerow(name)
