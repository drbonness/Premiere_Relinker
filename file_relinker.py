# Dan Bonness
# Neue Agency
# Philadelphia, PA
# September 21, 2017
# Function: Iterate through every line of a Premiere Project (xml file), replacing the names of previously imported files with their renamed counterparts. Relinks project to current files.
# Purpose: Allows Premiere to find footage and use current names.

import re
import csv
import sys
import math

def file_len(fname):    # get file length - number of lines
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

name_file = []

name_file.append(open("Output_1.csv","r")) # csv files to use for relinking
name_file.append(open("Output_2.csv","r"))

output_file = open("Output.xml","w")    # output xml to put relinked project file
read_file = "PHAN.xml"     # input xml to get project file

name_reader = [[],[]]

for x in range(len(name_file)): # for every csv file
    name_reader[x].append(csv.reader(name_file[x], delimiter=',', quotechar='"')); # read csv files

line_count = 0  # counts number of processed lines for progress bar
line_total = file_len(read_file)    # get the file length of the input xml
counter = [0,0]    # counts number of file 1 substitutions

for line in open(read_file,'r'):    # for every line in input xml

    output_line = line  # if nothing is altered, output_line will be same as input
    rep = 0;
    
    for x in range(len(name_file)):
        name_file[x].seek(0)  # start from beginning of file 1
        for csv_file in name_reader[x]: # get csv object from name_reader
            for row in csv_file: # get every row from the csv file
                [output_line,rep] = re.subn(str(row[0]), str(row[1]), line)  # replace file name; rep = 1 if success
                
                '''
                if(x == 0): # if first file
                    start_str = "A053_"
                    end_str = "_C" + ("{:03d}".format(int(row[0]))) + ".mov"
                    replace_string = row[1]+".mov"  # new file name
                    [output_line,rep] = re.subn(start_str+".*?"+end_str, replace_string, line)  # replace file name; rep = 1 if success
                if(x == 1): # if second file
                    file_string = str("C" + ("{:04d}".format(int(row[0]))) + ".MP4")
                    replace_string = row[1] + ".MP4"    # new file name
                    [output_line,rep] = re.subn(file_string, replace_string, str(line)) # replace file name; rep = 1 if success
                '''
                
                if(rep > 0): # if a file has been replaced
                    counter[x] = counter[x] + 1 # increment counter, specific to each file
                    break
        if(rep > 0): # if a file has been replaced
            break
                
    output_file.write(output_line)  # write the new line to output
    
    line_count = line_count + 1
    if(line_count % int(line_total/100) == 0):  # increment progress counter
        progress = int((line_count/float(line_total))*100)
        sys.stdout.write("Progress: %d%%   \r" % (progress))
        sys.stdout.flush()

for x in range(len(counter)):
    print("File " + str(x) + " Replacements:"+str(counter[x])) # print number of replacements

output_file.close
for x in range(len(name_file)):
    name_file[x].close