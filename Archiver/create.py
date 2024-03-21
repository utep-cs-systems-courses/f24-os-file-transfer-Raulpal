import os

# Creates tar file similar to command tar c file1 file2... > combined.tar
def outBandCreate(files):
    
    outMessage = "".encode()

    for file in files:
        if not os.path.exists("../Files/" +file.strip() ):                         # Check if path does not exist
            os.write(2,("File %s does not exist\n" % file).encode())
            exit()

        fdReader = os.open("../Files/" +file.strip(), os.O_RDONLY)               # Get file reader
    
        fileByteSize = os.path.getsize("../Files/" +file.strip())                # Get file byte size

        fileHeader = f"{file}\n{fileByteSize}\n".encode()   # Store header for file data

        contents = os.read(fdReader, fileByteSize)         # Get byte data

        outMessage += fileHeader
        outMessage += contents

        os.close(fdReader)                                  # Close when done

    return outMessage