import csv
def preRun(filt, filtNum):
    names = list()
    with open('names1.csv', 'r', encoding="utf-8") as data_file:
     csv_reader = csv.reader(data_file)
     for line in csv_reader:
            try:
                name = line[0]
                filtName = name.split(' ')[filtNum]
                if (filtName == filt):
                    names.append(name)
            except:
                pass

    with open('names1.csv', 'w', encoding='utf-8', newline='') as data_file:
         csv_writer = csv.writer(data_file)
         for name in names:
             line = [name]
             print(name)
             csv_writer.writerow(line)
    print(names.__len__())