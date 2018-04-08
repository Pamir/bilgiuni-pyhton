import  re

handle = open("access.log", "r")
exp = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
for line in handle:
    line = line
    y = re.findall(exp, line)
    if (len(y)):
        for ip in y:
            print(ip)
