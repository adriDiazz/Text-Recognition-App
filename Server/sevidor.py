
import socket
import pickle
import re
import json
def takeRawData(text):
    separator = r"\n"
    splited = text.split(separator)
    for palabra in splited:
        if palabra == "'":
            splited.remove(palabra)
    unido = ''.join(splited)

    splited2 = unido.split("'")

    for palabra in splited2:
        if palabra == "b":
            splited2.remove(palabra)
    rawData = ''.join(splited2)
    return rawData

HOST = '192.168.0.13'  # Standard loopback interface address (localhost)
PORT = 1085# Port to listen on (non-privileged ports are > 1023)
regex = re.compile("(\d{8})([A-Z])") 
nameRegex = re.compile('([A-Z]{1}[A-Z]{1,30}[- ]{0,1}|[A-Z]{1}[- \']{1}[A-Z]{0,1}[A-Z]{1,30}[- ]{0,1}|[A-Z]{1,2}[ -\']{1}[A-Z]{1}[A-Z]{1,30}){2,5}')
dateRegex = re.compile("(0?[1-9]|[12][0-9]|3[01])[ ](0?[1-9]|1[012])[ ]\d{4}")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)
            rawData = takeRawData(str(data))
            print(rawData)
            if (regex.match(rawData) or nameRegex.match(rawData) or dateRegex.match(data or data == "M" or data == "F")):
                with open('mensajess.json','w') as writer:
                    writer.write(rawData + "\n")
            if not data:
                break
    