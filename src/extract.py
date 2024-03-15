from io import BufferedReader, FileIO
import os, stat

# Extract from .tar  file into separate files
def outBandExtract(contents):

    # Split the contents into lines
    fcontentsList = contents.splitlines()

    updatedContents = ''

    # Check if there are enough lines for extraction
    if len(fcontentsList) >= 2:
        fname = fcontentsList.pop(0)  # Remove and get the first line (filename)
        fsize = fcontentsList.pop(0)  # Remove and get the second line (file size)
        fcontents = fcontentsList.pop(0)  # Remove and get the third line (file contents)

        updatedContents = '\n'.join(fcontentsList)
        return (fname, fcontents, updatedContents)  # return the filename and file content and updated data
    else:
        print("Corrupted file")
        return  (None, None,updatedContents)

