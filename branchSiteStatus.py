import csvhandler
from tqdm import tqdm

write = csvhandler.Write()
read = csvhandler.Read()
# inputs
inp = read.dataFrame('/mnt/c/Work/NACE/data/miskolc_out_in.csv')
miskolc = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]
inp2 = read.dataFrame('/mnt/c/Work/NACE/data/miskolc_branchout.csv')
miskolcBranch = [csvhandler.Dict(i, inp2[0]) for i in inp2[1:]]
inp3 = read.dataFrame('/mnt/c/Work/NACE/data/miskolc_sitesout.csv')
miskolcSites = [csvhandler.Dict(i, inp3[0]) for i in inp3[1:]]
# outputs
out1 = '/mnt/c/Work/NACE/data/miskolc_branches_out.csv'
out2 = '/mnt/c/Work/NACE/data/miskolc_sites_out.csv'
head1 = write.header(miskolcBranch)
head2 = write.header(miskolcSites)
##############################################################


def calculateBranch(miskolc, miskolcBranch):
    print("Calculations with Branches in miskolc:")
    for i in tqdm(range(len(miskolcBranch))):
        for j in range(len(miskolc)):
            if miskolcBranch[i].ID.strip() == miskolc[j].ID.strip():
                miskolcBranch[i].SECTION = miskolc[j].SECTION
                miskolcBranch[i].DIVISION = miskolc[j].DIVISION
                miskolcBranch[i].GROUP = miskolc[j].GROUP
                miskolcBranch[i].CLASS = miskolc[j].CLASS
                miskolcBranch[i].LegalStatus = miskolc[j].LegalStatus
                miskolcBranch[i].ActiveFrom = miskolc[j].ActiveFrom
                miskolcBranch[i].ActiveUntil = miskolc[j].ActiveUntil

    print("Miskolc done.")
    return miskolcBranch


def calculateSites(miskolc, miskolcSites):
    print("Calculations with Sites in miskolc:")
    for i in tqdm(range(len(miskolcSites))):
        for j in range(len(miskolc)):
            if miskolcSites[i].ID.strip() == miskolcSites[j].ID.strip():
                miskolcSites[i].SECTION = miskolc[j].SECTION
                miskolcSites[i].DIVISION = miskolc[j].DIVISION
                miskolcSites[i].GROUP = miskolc[j].GROUP
                miskolcSites[i].CLASS = miskolc[j].CLASS
                miskolcSites[i].LegalStatus = miskolc[j].LegalStatus
                miskolcSites[i].ActiveFrom = miskolc[j].ActiveFrom
                miskolcSites[i].ActiveUntil = miskolc[j].ActiveUntil

    print("Miskolc done.")
    return miskolcSites


def Writer1(output, head, data):
    print("Writing Miskolc-out")
    write.writer(output, head, data)


def Writer2(output, head, data):
    print("Writing Miskolc-out")
    write.writer(output, head, data)


# for debugging purposes:
if __name__ == '__main__':
    calculateBranch(miskolc, miskolcBranch)
    Writer1(out1, head1, miskolcBranch)
    calculateSites(miskolc, miskolcSites)
    Writer2(out2, head2, miskolcSites)
    print(" ")
