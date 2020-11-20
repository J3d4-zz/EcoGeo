import csvhandler
from tqdm import tqdm

write = csvhandler.Write()
read = csvhandler.Read()

inp = read.dataframe('/mnt/d/Work/NACE/data/miskolc_out_in.csv')
miskolc = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]
out = '/mnt/d/Work/NACE/data/miskolc_out_out.csv'
branchOut = '/mnt/d/Work/NACE/data/miskolc_branchout.csv'
sitesOut = '/mnt/d/Work/NACE/data/miskolc_sitesout.csv'
head = write.header(miskolc)
##############################################################

ID, branch, sites, sepBranch, sepSites = []


def calculate(miskolc):
    print("Calculations with miskolc in miskolc:")
    for i in tqdm(range(len(miskolc))):
        ID.append(miskolc[i].ID)
        branch.append(miskolc[i].Branch_locations.split(" / "))
        sites.append(miskolc[i].Sites.split(" / "))

    print("Miskolc done.")
    return miskolc


# def writer(output, head, data):
#     print("Writing Miskolc-out")
#     write.writer(output, head, data)


def dataWriter(output, head, data):
    print("Writing Miskolc-out")
    write.dataWriter(output, head, data)


def dataWriter2(output, head, data):
    print("Writing Miskolc-out")
    write.dataWriter(output, head, data)


# for debugging purposes:
if __name__ == '__main__':
    calculate(miskolc)
    for i in range(len(ID)):
        for j in range(len(branch[i])):
            sepBranch.append({"ID": ID[i], "Branch": branch[i][j]})
        for j in range(len(sites[i])):
            sepSites.append({"ID": ID[i], "Sites": sites[i][j]})
    branchHead = ["ID", "Branch"]
    dataWriter(branchOut, branchHead, sepBranch)
    sitesHead = ["ID", "Sites"]
    dataWriter2(sitesOut, sitesHead, sepSites)
    ## writer(out, head, miskolc)
    print(" ")
