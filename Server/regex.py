import re
regex = re.compile("(\d{8})([A-Z])")
#nameRegex = re.compile('([A-Z]{1}[a-z]{1,30}[- ]{0,1}|[A-Z]{1}[- \']{1}[A-Z]{0,1}[a-z]{1,30}[- ]{0,1}|[a-z]{1,2}[ -\']{1}[A-Z]{1}[a-z]{1,30}){2,5}')
nameRegex = re.compile('([A-Z]{1}[A-Z]{1,30}[- ]{0,1}|[A-Z]{1}[- \']{1}[A-Z]{0,1}[A-Z]{1,30}[- ]{0,1}|[A-Z]{1,2}[ -\']{1}[A-Z]{1}[A-Z]{1,30}){2,5}')
dateRegex = re.compile("(0?[1-9]|[12][0-9]|3[01])[ ](0?[1-9]|1[012])[ ]\d{4}")

#find = re.search("/^(\d{8})([A-Z])$/","mensajes.txt")
#print(find)



textfile = open('mensajes.txt', 'r')
filetext = textfile.read()
textfile.close()

if (dateRegex.match(filetext)):
    print ("yessss")