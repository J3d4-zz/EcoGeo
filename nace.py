import csvhandler
from tqdm import tqdm

write = csvhandler.Write()
read = csvhandler.Read()

inp = read.dataFrame('/mnt/d/Work/NACE/data/miskolc_out_in.csv')
miskolc = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]
inp2 = read.dataFrame('/mnt/d/Work/NACE/data/nace.csv')
nace = [csvhandler.Dict(i, inp2[0]) for i in inp2[1:]]
out = '/mnt/d/Work/NACE/data/miskolc_out_out.csv.csv'
head = write.header(miskolc)
##############################################################


def calculate(nace, miskolc):
    print("Calculations with nace in miskolc:")
    for i in tqdm(range(len(miskolc))):
        for j in range(len(nace)):
            if miskolc[i].TEAOR08_fixed.strip() == nace[j].Kod.strip():
                miskolc[i].SECTION = nace[j].SECTION
                miskolc[i].DIVISION = nace[j].DIVISION
                miskolc[i].GROUP = nace[j].GROUP
                miskolc[i].CLASS = nace[j].CLASS

    print("Miskolc done.")
    return miskolc


def writer(output, head, data):
    print("Writing Miskolc-out")
    write.writer(output, head, data)
    print("Done.")


# for debugging purposes:
if __name__ == '__main__':
    calculate(nace, miskolc)
    writer(out, head, miskolc)
    print(" ")
