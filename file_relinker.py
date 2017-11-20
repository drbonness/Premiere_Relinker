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
import os

def file_len(fname):    # get file length - number of lines
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

name_file = []
name_file.append(open("Output_1.csv","r")) # csv files to use for relinking

output_file = open("Output.xml","w")        # output xml to put relinked project file
read_file = "MOBILE OUTFITTERS NEW.xml"     # input xml to get project file

line_count = 0  # counts number of processed lines for progress bar
line_total = file_len(read_file)    # get the file length of the input xml
counter = []    # counts number of file type subsitutions

name_reader = [] # list for storing csv file information
file_extensions = [] # list for storing file extension types

csv_text = list((csv.reader(name_file[0], delimiter=',', quotechar='"')))

for x in range(len(csv_text)): # for every csv file
    filename, extension = os.path.splitext(csv_text[x][0]) # split the path to find the files extension type
    
    if extension not in file_extensions:    # if the extension is not in the array file_extensions
        file_extensions.append(extension)   # add it to file_extensions
        name_reader.append([]) # read csv files
        counter.append(0) # create a counter for every file type
    
    name_reader[file_extensions.index(extension)].append(csv_text[x]); # read csv files
    
for line in open(read_file,'r'):    # for every line in input xml

    output_line = line  # if nothing is altered, output_line will be same as input
    rep = 0;
    
    for x in range(len(file_extensions)):
        
        if(rep > 0): # if a file has been replaced
            break
        
        found_match = re.search(file_extensions[x], line)  # search for extension type in line; found_match is not None if success
        if(found_match is not None): # if the extension type was found
            for y in range(len(name_reader[x])): # check every file with the same extension type
                [output_line,rep] = re.subn(name_reader[x][y][0], name_reader[x][y][1], line)  # replace file name; rep = 1 if success
                if(rep > 0): # if a file has been replaced
                    counter[x] = counter[x] + 1 # increment counter, specific to each file
                    break
                
    output_file.write(output_line)  # write the new line to output
    
    line_count = line_count + 1
    if(line_count == 1):
        progress = int((line_count/float(line_total))*100)
        sys.stdout.write("Progress: %d%%   \r" % (progress))
        sys.stdout.flush()
    if(line_count % int(line_total/100) == 0):  # increment progress counter
        progress = int((line_count/float(line_total))*100)
        sys.stdout.write("Progress: %d%%   \r" % (progress))
        sys.stdout.flush()

for x in range(len(counter)):
    print(file_extensions[x] + " Replacements: "+str(counter[x])) # print number of replacements

output_file.close
for x in range(len(name_file)):
    name_file[x].close

'''
DEPRECATED CODE----------------------------------------------------------

USING MULTIPLE CSV FILES

#name_file.append(open("Output_2.csv","r")) # deprecated, only use one csv file
#name_file.append(open("Output_3.csv","r"))

UNKNOWN EXACT FILE NAMES

if(x == 0): # if first file
    start_str = "A053_"
    end_str = "_C" + ("{:03d}".format(int(row[0]))) + ".mov"
    replace_string = row[1]+".mov"  # new file name
    [output_line,rep] = re.subn(start_str+".*?"+end_str, replace_string, line)  # replace file name; rep = 1 if success
if(x == 1): # if second file
    file_string = str("C" + ("{:04d}".format(int(row[0]))) + ".MP4")
    replace_string = row[1] + ".MP4"    # new file name
    [output_line,rep] = re.subn(file_string, replace_string, str(line)) # replace file name; rep = 1 if success


for x in range(len(name_file)):
    name_file[x].seek(0)  # start from beginning of file 1
    for csv_file in name_reader[x]: # get csv object from name_reader
        for row in csv_file: # get every row from the csv file
            [output_line,rep] = re.subn(str(row[0]), str(row[1]), line)  # replace file name; rep = 1 if success

            if(rep > 0): # if a file has been replaced
                counter[x] = counter[x] + 1 # increment counter, specific to each file
                break
    if(rep > 0): # if a file has been replaced
        break


'''
                