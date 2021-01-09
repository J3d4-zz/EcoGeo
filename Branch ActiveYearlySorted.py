import csvhandler
from tqdm import tqdm

write = csvhandler.Write()
read = csvhandler.Read()
# inputs
inp = read.dataFrame('/mnt/c/Work/NACE/data/miskolc_out_in3.csv')
miskolc = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]
# outputs
out1 = '/mnt/c/Work/NACE/data/miskolc_out_in4.csv'
head1 = write.header(miskolc)
##############################################################


def calculateBranch(miskolc):
    print("Calculations with Branches:")
    for i in tqdm(range(len(miskolc))):
        ActiveFromYear = 0
        ActiveUntilYear = 3000
        
        if(miskolc[i].ActiveUntilYear != ""):
            ActiveUntilYear = int(miskolc[i].ActiveUntilYear)
        if(miskolc[i].ActiveFromYear != ""):
            ActiveFromYear = int(miskolc[i].ActiveFromYear)
        
        if("miskolc" in miskolc[i].Headquarter or "Miskolc" in miskolc[i].Headquarter):
            if(ActiveUntilYear >= 2018):
                if(ActiveFromYear <= 2018):
                    miskolc[i].Active2018 = 1
                else:
                    miskolc[i].Active2018 = 0
            else:
                miskolc[i].Active2018 = 0
            if(ActiveUntilYear >= 2017):
                if(ActiveFromYear <= 2017):
                    miskolc[i].Active2017 = 1
                else:
                    miskolc[i].Active2017 = 0
            else:
                miskolc[i].Active2017 = 0
            if(ActiveUntilYear >= 2016):
                if(ActiveFromYear <= 2016):
                    miskolc[i].Active2016 = 1
                else:
                    miskolc[i].Active2016 = 0
            else:
                miskolc[i].Active2016 = 0
            if(ActiveUntilYear >= 2015):
                if(ActiveFromYear <= 2015):
                    miskolc[i].Active2015 = 1
                else:
                    miskolc[i].Active2015 = 0
            else:
                miskolc[i].Active2015 = 0
            if(ActiveUntilYear >= 2014):
                if(ActiveFromYear <= 2014):
                    miskolc[i].Active2014 = 1
                else:
                    miskolc[i].Active2014 = 0
            else:
                miskolc[i].Active2014 = 0
            if(ActiveUntilYear >= 2013):
                if(ActiveFromYear <= 2013):
                    miskolc[i].Active2013 = 1
                else:
                    miskolc[i].Active2013 = 0
            else:
                miskolc[i].Active2013 = 0
            if(ActiveUntilYear >= 2012):
                if(ActiveFromYear <= 2012):
                    miskolc[i].Active2012 = 1
                else:
                    miskolc[i].Active2012 = 0
            else:
                miskolc[i].Active2012 = 0
            if(ActiveUntilYear >= 2011):
                if(ActiveFromYear <= 2011):
                    miskolc[i].Active2011 = 1
                else:
                    miskolc[i].Active2011 = 0
            else:
                miskolc[i].Active2011 = 0
            if(ActiveUntilYear >= 2010):
                if(ActiveFromYear <= 2010):
                    miskolc[i].Active2010 = 1
                else:
                    miskolc[i].Active2010 = 0
            else:
                miskolc[i].Active2010 = 0
            if(ActiveUntilYear >= 2009):
                if(ActiveFromYear <= 2009):
                    miskolc[i].Active2009 = 1
                else:
                    miskolc[i].Active2009 = 0
            else:
                miskolc[i].Active2009 = 0
            if(ActiveUntilYear >= 2008):
                if(ActiveFromYear <= 2008):
                    miskolc[i].Active2008 = 1
                else:
                    miskolc[i].Active2008 = 0
            else:
                miskolc[i].Active2008 = 0
        else:
            miskolc[i].Active2008 = 0
            miskolc[i].Active2009 = 0
            miskolc[i].Active2010 = 0
            miskolc[i].Active2011 = 0
            miskolc[i].Active2012 = 0
            miskolc[i].Active2013 = 0
            miskolc[i].Active2014 = 0
            miskolc[i].Active2015 = 0
            miskolc[i].Active2016 = 0
            miskolc[i].Active2017 = 0
            miskolc[i].Active2018 = 0
        
        # miskolc[i].ActiveFromYear = miskolc[i].ActiveFrom[-4:]
        # miskolc[i].ActiveUntilYear = miskolc[i].ActiveUntil[-4:]

    print("Miskolc done.")
    return miskolc


def Writer(output, head, data):
    print("Writing Miskolc-out")
    write.writer(output, head, data)

# for debugging purposes:
if __name__ == '__main__':
    calculateBranch(miskolc)
    Writer(out1, head1, miskolc)
    print(" ")
