import csv
from tqdm import tqdm


class Dict:
    def __init__(self, row, header):
        self.__dict__ = dict(zip(header, row))


class Read:
    def dataFrame(self, file):
        return list(csv.reader(open(file, 'r', encoding='utf-8'), delimiter=','))


class Write:
    def header(self, data):
        value = list()
        for i in data[1].__dict__:
            value.append(i)
        return value

    def writer(self, file, header, data):
        write = csv.DictWriter(
            open(file, 'w', encoding='utf-8'), delimiter=',', fieldnames=header)
        write.writeheader()
        for i in tqdm(range(len(data))):
            write.writerow(data[i].__dict__)

    def dataWriter(self, file, header, data):
        write = csv.DictWriter(
            open(file, 'w', encoding='utf-8'), delimiter=',', fieldnames=header)
        write.writeheader()
        for i in tqdm(data):
            write.writerow(i)
