## This script will strip out time information from transcription files of a particular pattern
## For example, the following will be removed from a text file:
##  1
##  00:00:00,970 --> 00:00:02,040

import glob, os, re

# change to directory of script
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

for file in glob.glob("*.txt"):
    processedFileName = file.replace('.txt', '') + "_processed" + ".txt";

    # return number of lines from original file
    f = open(file,"r")
    lines = f.readlines()
    f.close()
    originalFileLineCount=len(lines)


    # open new processed file
    try:
        os.mkdir('processed')
    except:
        pass

    f = open('processed/'+ processedFileName, "w")
    f.truncate()
    pattern1 = '^\d+$'
    pattern2 = '^\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d$'

    processedFileLineCount = 0
    previousLine=''
    for line in lines:
        #print(line)
        #match = re.match(pattern1, line) > 0
        # if type(match)~=None:
        if re.match(pattern1, line) or re.match(pattern2, line) or line == '\n':
            #print(line)
            pass
        else:
            f.write(line)
            f.write('\n')
            processedFileLineCount += 2

    f.close()

    print(file + ': ' + str(originalFileLineCount) + ' lines')
    print(processedFileName + ': ' + str(processedFileLineCount) + ' lines')