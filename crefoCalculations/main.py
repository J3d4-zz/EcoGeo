import csvhandler
from tqdm import tqdm

write = csvhandler.Write()
read = csvhandler.Read()

inp = read.dataFrameWindowsSemiColon(
    '/mnt/d/Work/NACE/orszagosDB/branches.txt')
branchesDataFrame = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]
out = '/mnt/d/Work/NACE/data/crefoBranchCleaned.csv'
head = write.header(branchesDataFrame)
#################################################################


def calculate(branchesDataFrame):
    print("Calculations with branchesDataFrame in branchesDataFrame:")
    for i in tqdm(range(len(branchesDataFrame))):
        Crefoszam = branchesDataFrame[i].Crefoszám
        Adoszam = branchesDataFrame[i].Adószám.strip(" ' ")
        CimTipusKod = branchesDataFrame[i].Címtípuskód.strip(" ' ")
        CimTipus = branchesDataFrame[i].Címtípus.strip(" ' ")
        OrszagKod = branchesDataFrame[i].Országkód.strip(" ' ")
        Orszag = branchesDataFrame[i].Ország.strip(" ' ")
        Iranyitoszam = branchesDataFrame[i].Irányítószám.strip(" ' ")
        Telepules = branchesDataFrame[i].Település.strip(" ' ")
        Utca = branchesDataFrame[i].Utca.strip(" ' ")
        Hazszam = branchesDataFrame[i].Házszám.strip(" ' ")
        ErvenyessegKezdete = branchesDataFrame[i].Érvényességkezdete.strip(
            " ' ")
        ErvenyessegVege = branchesDataFrame[i].Érvényességvége.strip(" ' ")

        branchesDataFrame[i].Crefoszám = Crefoszam
        branchesDataFrame[i].Adószám = Adoszam
        branchesDataFrame[i].Címtípuskód = CimTipusKod
        branchesDataFrame[i].Címtípus = CimTipus
        branchesDataFrame[i].Országkód = OrszagKod
        branchesDataFrame[i].Ország = Orszag
        branchesDataFrame[i].Irányítószám = Iranyitoszam
        branchesDataFrame[i].Település = Telepules
        branchesDataFrame[i].Utca = Utca
        branchesDataFrame[i].Házszám = Hazszam
        branchesDataFrame[i].Érvényességkezdete = ErvenyessegKezdete
        branchesDataFrame[i].Érvényességvége = ErvenyessegVege

    print("Calculations done.")
    return branchesDataFrame


def dataWriter(output, head, data):
    print("Writing Data-out")
    write.writer(output, head, data)


# for debugging purposes:
if __name__ == '__main__':
    calculate(branchesDataFrame)
    dataWriter(out, head, branchesDataFrame)
    print(" ")
