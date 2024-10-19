
import re

ip = "192.168.2.1\\24"
ip = ip.replace("."," ")
print(ip)
print(re.split("\s",ip))