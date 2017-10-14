# Premiere_Relinker

This repo allows you to quickly relink all of the media in a Premiere Pro project file without manually finding it. Useful if files are renamed while linked to a Premiere Pro project.

Note:
For the python code in this repo to function, it must be able to access the xml code from a Premiere Pro project file. However, Premiere Pro project (.prproj) files are not, in themselves xml files. Here is the method for conversion:

Premiere Pro File → XML
1. .prproj → .gz        // Change the extension of the file to .gz (gzip)
2. Unzip                // Unzip the gzip file (double click on a Mac)
3. \+ .xml              // Add .xml as the file extension of the unzipped file (starts with no extension)

XML → Premiere Pro File
1. Gzip                                     // Gzip the output xml file
    - Mac Terminal Input: gzip Output.xml
2. .gz → .prproj                            // Change the extension of the file to .prproj


## file_name_finder.py ##

This file allows you to quickly extract all of the file names in a given directory (excluding hidden files). Files are ordered by modification date, because the modification date of a file remains unchanged when a file name is changed.

If an input file (typically a previous output) is specified, file names will be appended to the input file. This creates a CSV output file where:

Columns:
1. Original File Names (Input)
2. New File Names

If no input file is specified, the program will produce a 1-Column CSV file containing all of file names in the given directory. Therefore it is advisable to run this program, without an input file, to produce an "Original File Name" output file, before renaming any files.

## file_relinker.py ##

This file takes a 2-Column CSV file as input. It searches through an input file (xml,txt,etc...) and replaces Text from Column 1 with Text from Column 2.

When using the reccomended input, it will relink all of the media in a Premiere Pro project file, replacing original file names with new file names.

Reccomended Input:
* XML file
    * Converted Premiere Pro Project File
* CSV file
    * Column 1 = Original File Names
    * Column 2 = New File Names
