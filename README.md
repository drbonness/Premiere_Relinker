# Premiere_Relinker

This repo allows you to quickly relink all of the media in a Premiere Pro project file without manually finding it. Useful if files are renamed while linked to a Premiere Pro project.

Note:
For the python code in this repo to function, it must be able to access the xml code from a Premiere Pro project file. However, Premiere Pro project (.prproj) files are not, in themselves xml files. Here is the method for conversion:

Premiere Pro File --> XML
1. .prproj --> .gz    // Change the extension of the file to .gz (gzip)
2. Unzip              // Unzip the gzip file (double click on a Mac)
3. + .xml             // Add .xml as the file extension of the unzipped file (starts with no extension)

XML --> Premiere Pro File
1. Gzip                                       // Gzip the output xml file
    - Mac Terminal Input: gzip Output.xml
2. .gz --> .prproj                            // Change the extension of the file to .prproj


# file_name_finder.py

# file_relinker.py

