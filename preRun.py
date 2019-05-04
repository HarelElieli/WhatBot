import csv

def preRun(filt, filtNum, pathBase, namesToDo_fileName):
    filePath = pathBase % namesToDo_fileName
    names = list()
    with open(filePath, 'r', encoding="utf-8") as data_file:
     csv_reader = csv.reader(data_file)
     for line in csv_reader:
            try:
                name = line[0]
                filtName = name.split(' ')[filtNum]
                if (filtName == filt):
                    names.append(name)
            except:
                pass

    with open(filePath, 'w', encoding='utf-8', newline='') as data_file:
         csv_writer = csv.writer(data_file)
         for name in names:
             line = [name]
             csv_writer.writerow(line)
    print(str(names.__len__()) + ' messages to go.')