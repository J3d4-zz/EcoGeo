import csvhandler
from tqdm import tqdm

write = csvhandler.Write()
read = csvhandler.Read()
# inputs
inp = read.dataFrame('/mnt/c/Work/NACE/data/Miskolc.csv')
miskolc = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]
inp2 = read.dataFrame('/mnt/c/Work/NACE/data/miskolc_out_in.csv')
miskolcBranch = [csvhandler.Dict(i, inp2[0]) for i in inp2[1:]]
# outputs
out1 = '/mnt/c/Work/NACE/data/miskolc_branches_out_in2.csv'
head1 = write.header(miskolcBranch)
##############################################################


def calculateBranch(miskolc, miskolcBranch):
    print("Calculations with Branches in miskolc:")
    for i in tqdm(range(len(miskolcBranch))):
        for j in range(len(miskolc)):
            if miskolcBranch[i].ID.strip() == miskolc[j].ID.replace(" ", ""):
                miskolcBranch[i].LegalStatus = miskolc[j].LegalStatus
                miskolcBranch[i].ActiveFrom = miskolc[j].ActiveFrom
                miskolcBranch[i].ActiveUntil = miskolc[j].ActiveUntil

    print("Miskolc done.")
    return miskolcBranch


def Writer(output, head, data):
    print("Writing Miskolc-out")
    write.writer(output, head, data)

# for debugging purposes:
if __name__ == '__main__':
    calculateBranch(miskolc, miskolcBranch)
    Writer(out1, head1, miskolcBranch)
    print(" ")
