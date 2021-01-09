import csvhandler
from tqdm import tqdm

write = csvhandler.Write()
read = csvhandler.Read()
# inputs
inp = read.dataFrame('/mnt/d/Work/NACE/data/miskolc_branches_out4.csv')
miskolc = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]
inp2 = read.dataFrame('/mnt/d/Work/NACE/data/nace.csv')
nace = [csvhandler.Dict(i, inp2[0]) for i in inp2[1:]]
# outputs
out1 = '/mnt/d/Work/NACE/data/miskolc_branches_out_in_sum.csv'
head1 = write.header(nace)
##############################################################


def calculateBranch(miskolc, nace):
    print("Calculating -> ")
    for i in tqdm(range(len(nace))):
        Active2008Sum = 0
        Active2009Sum = 0
        Active2010Sum = 0
        Active2011Sum = 0
        Active2012Sum = 0
        Active2013Sum = 0
        Active2014Sum = 0
        Active2015Sum = 0
        Active2016Sum = 0
        Active2017Sum = 0
        Active2018Sum = 0
        for j in range(len(miskolc)):
            Active2008 = int(miskolc[j].Active2008)
            Active2009 = int(miskolc[j].Active2009)
            Active2010 = int(miskolc[j].Active2010)
            Active2011 = int(miskolc[j].Active2011)
            Active2012 = int(miskolc[j].Active2012)
            Active2013 = int(miskolc[j].Active2013)
            Active2014 = int(miskolc[j].Active2014)
            Active2015 = int(miskolc[j].Active2015)
            Active2016 = int(miskolc[j].Active2016)
            Active2017 = int(miskolc[j].Active2017)
            Active2018 = int(miskolc[j].Active2018)
            if miskolc[j].CLASS != '' and nace[i].CLASS != '' and miskolc[j].CLASS.strip(' ') == nace[i].CLASS.strip(' '):
                Active2008Sum = Active2008Sum + Active2008
                Active2009Sum = Active2009Sum + Active2009
                Active2010Sum = Active2010Sum + Active2010
                Active2011Sum = Active2011Sum + Active2011
                Active2012Sum = Active2012Sum + Active2012
                Active2013Sum = Active2013Sum + Active2013
                Active2014Sum = Active2014Sum + Active2014
                Active2015Sum = Active2015Sum + Active2015
                Active2016Sum = Active2016Sum + Active2016
                Active2017Sum = Active2017Sum + Active2017
                Active2018Sum = Active2018Sum + Active2018
                nace[i].Active2008Sum = Active2008Sum
                nace[i].Active2009Sum = Active2009Sum
                nace[i].Active2010Sum = Active2010Sum
                nace[i].Active2011Sum = Active2011Sum
                nace[i].Active2012Sum = Active2012Sum
                nace[i].Active2013Sum = Active2013Sum
                nace[i].Active2014Sum = Active2014Sum
                nace[i].Active2015Sum = Active2015Sum
                nace[i].Active2016Sum = Active2016Sum
                nace[i].Active2017Sum = Active2017Sum
                nace[i].Active2018Sum = Active2018Sum
    print("Done.")
    return nace


def Writer(output, head, data):
    print("Writing data out")
    write.writer(output, head, data)
    print("Done")


# for debugging purposes:
if __name__ == '__main__':
    calculateBranch(miskolc, nace)
    Writer(out1, head1, nace)
    print(" ")
