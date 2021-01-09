import csvhandler
from tqdm import tqdm

write = csvhandler.Write()
read = csvhandler.Read()
# inputs
inp2 = read.dataFrame('/mnt/c/Work/NACE/data/miskolc_branches_out3.csv')
miskolcBranch = [csvhandler.Dict(i, inp2[0]) for i in inp2[1:]]
# outputs
out1 = '/mnt/c/Work/NACE/data/miskolc_branches_out4.csv'
head1 = write.header(miskolcBranch)
##############################################################


def calculateBranch(miskolcBranch):
    print("Calculations with Branches:")
    for i in tqdm(range(len(miskolcBranch))):
        ActiveFromYear = 0
        ActiveUntilYear = 3000
        
        if(miskolcBranch[i].ActiveUntilYear != ""):
            ActiveUntilYear = int(miskolcBranch[i].ActiveUntilYear)
        if(miskolcBranch[i].ActiveFromYear != ""):
            ActiveFromYear = int(miskolcBranch[i].ActiveFromYear)
        
        if("miskolc" in miskolcBranch[i].Branch or "Miskolc" in miskolcBranch[i].Branch):
            if(ActiveUntilYear >= 2018):
                if(ActiveFromYear <= 2018):
                    miskolcBranch[i].Active2018 = 1
                else:
                    miskolcBranch[i].Active2018 = 0
            else:
                miskolcBranch[i].Active2018 = 0
            if(ActiveUntilYear >= 2017):
                if(ActiveFromYear <= 2017):
                    miskolcBranch[i].Active2017 = 1
                else:
                    miskolcBranch[i].Active2017 = 0
            else:
                miskolcBranch[i].Active2017 = 0
            if(ActiveUntilYear >= 2016):
                if(ActiveFromYear <= 2016):
                    miskolcBranch[i].Active2016 = 1
                else:
                    miskolcBranch[i].Active2016 = 0
            else:
                miskolcBranch[i].Active2016 = 0
            if(ActiveUntilYear >= 2015):
                if(ActiveFromYear <= 2015):
                    miskolcBranch[i].Active2015 = 1
                else:
                    miskolcBranch[i].Active2015 = 0
            else:
                miskolcBranch[i].Active2015 = 0
            if(ActiveUntilYear >= 2014):
                if(ActiveFromYear <= 2014):
                    miskolcBranch[i].Active2014 = 1
                else:
                    miskolcBranch[i].Active2014 = 0
            else:
                miskolcBranch[i].Active2014 = 0
            if(ActiveUntilYear >= 2013):
                if(ActiveFromYear <= 2013):
                    miskolcBranch[i].Active2013 = 1
                else:
                    miskolcBranch[i].Active2013 = 0
            else:
                miskolcBranch[i].Active2013 = 0
            if(ActiveUntilYear >= 2012):
                if(ActiveFromYear <= 2012):
                    miskolcBranch[i].Active2012 = 1
                else:
                    miskolcBranch[i].Active2012 = 0
            else:
                miskolcBranch[i].Active2012 = 0
            if(ActiveUntilYear >= 2011):
                if(ActiveFromYear <= 2011):
                    miskolcBranch[i].Active2011 = 1
                else:
                    miskolcBranch[i].Active2011 = 0
            else:
                miskolcBranch[i].Active2011 = 0
            if(ActiveUntilYear >= 2010):
                if(ActiveFromYear <= 2010):
                    miskolcBranch[i].Active2010 = 1
                else:
                    miskolcBranch[i].Active2010 = 0
            else:
                miskolcBranch[i].Active2010 = 0
            if(ActiveUntilYear >= 2009):
                if(ActiveFromYear <= 2009):
                    miskolcBranch[i].Active2009 = 1
                else:
                    miskolcBranch[i].Active2009 = 0
            else:
                miskolcBranch[i].Active2009 = 0
            if(ActiveUntilYear >= 2008):
                if(ActiveFromYear <= 2008):
                    miskolcBranch[i].Active2008 = 1
                else:
                    miskolcBranch[i].Active2008 = 0
            else:
                miskolcBranch[i].Active2008 = 0
        else:
            miskolcBranch[i].Active2008 = 0
            miskolcBranch[i].Active2009 = 0
            miskolcBranch[i].Active2010 = 0
            miskolcBranch[i].Active2011 = 0
            miskolcBranch[i].Active2012 = 0
            miskolcBranch[i].Active2013 = 0
            miskolcBranch[i].Active2014 = 0
            miskolcBranch[i].Active2015 = 0
            miskolcBranch[i].Active2016 = 0
            miskolcBranch[i].Active2017 = 0
            miskolcBranch[i].Active2018 = 0
        
        # miskolcBranch[i].ActiveFromYear = miskolcBranch[i].ActiveFrom[-4:]
        # miskolcBranch[i].ActiveUntilYear = miskolcBranch[i].ActiveUntil[-4:]

    print("Miskolc done.")
    return miskolcBranch


def Writer(output, head, data):
    print("Writing Miskolc-out")
    write.writer(output, head, data)

# for debugging purposes:
if __name__ == '__main__':
    calculateBranch(miskolcBranch)
    Writer(out1, head1, miskolcBranch)
    print(" ")
