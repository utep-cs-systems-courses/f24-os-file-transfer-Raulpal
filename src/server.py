#! /usr/bin/env python3

import socket, sys, re
sys.path.append("../lib")       # for params
import params
from extract import outBandExtract
import io

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )



progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddr = ''       # Symbolic name meaning all available interfaces

if paramMap['usage']:
    params.usage()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((listenAddr, listenPort))
s.listen(1)              # allow only one outstanding request

conn, addr = s.accept()  # wait until incoming connection request (and accept it)
print('Connected by', addr)

while True:
    data = conn.recv(1024)  # Receive data from the client

    if not data:
        print("Zero length read, nothing to send, terminating")
        break

    while True:
        if isinstance(data, bytes):
            data = data.decode()  # Decode bytes to string if needed
        fname, fData, data = outBandExtract(data) 
        
        # Check if extraction was successful
        if fname is not None and fData is not None:
            sendMsg = b"Echoing " + fname.encode() + b" " + fData.encode() + b"\n"  # Append "Echoing " to the received data
            print("Received file name '%s' with contents '%s', sending '%s'" % (fname, fData, sendMsg))
            conn.sendall(sendMsg)  # Send the modified data back to the client
        if not data:   
            break
conn.shutdown(socket.SHUT_WR)
conn.close()