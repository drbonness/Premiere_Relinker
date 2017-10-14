# Dan Bonness
# Neue Agency
# Philadelphia, PA
# September 21, 2017
# Function: Write the names of all the files (with a certain file type) in a directory, ordered by modification date, to a csv
# Purpose: The modification date of footage should not change when it is renamed. This program should give the original order of footage files after they have been renamed. Use this program in conjunction with the Premiere file relinker program.

import os
import tkFileDialog
import Tkinter

root = Tkinter.Tk()
root.withdraw() #use to hide tkinter window

# path = "/Users/danbonness/Desktop/Saved Files/SD Card/VIDEO/Ursinus" # input directory, '.' for current

path = tkFileDialog.askdirectory() # input directory
csv_name = "Output_1.csv" # name of input csv file
append_fn = True    # append list to existing file, if False write new file

line_count = 0 # number of lines
write_count = 0    # counts the number of filtered files written to csv
start_num = 1   # number that is incremented (corresponds to the ending number of the original files)
f = []  # file names
e = []  # original input lines from csv file (if appending)

if(append_fn):  # if the file is being appended
    if(os.path.isfile(csv_name)):   # check it's a file
        for line in open(csv_name,'r'): # read the current contents of the file
            e.append(line.strip())
            line_count = line_count + 1

for (dirpath, _, filenames) in os.walk(path):   # walk through the directory and find all files (includes files in subdir)
    f.extend([filename,os.path.getmtime(os.path.join(dirpath,filename))]for filename in filenames)

f = sorted(f, key=lambda x: x[1])   # sort files by last modification date (typically corresponds to original order)

output_file = open("Output.csv","w")    # open the output file

for x in range(len(f)): # for every file in f
    
    if(not f[x][0].startswith(".")):   # if it is the correct file type
        if (write_count > 0): output_file.write("\n")   # if it's not the first line, start a new line
        if(append_fn):  # if appending to previous file
            if(write_count < line_count): # if x < the length of the previous file
                    output_file.write(e[write_count]+","+str(f[x][0]))    # append new file names to previous file
            else:
                if(e!=[]):  # if there was something written in the previous file
                    output_file.write(","+str(f[x][0])) # include a comma before writing new files names
                else:   # otherwise
                    output_file.write(str(f[x][0])) # only write new file names
        else:   # otherwise, if not appending to previous file
            output_file.write(str(start_num+write_count)+","+str(f[x][0]))  # write "[increasing number],[file name]"
        write_count = write_count + 1   # increment counter for files written to csv
      
output_file.close
