from ping3 import ping
import json
import threading
import encodings.idna

def myping(host, name):
    try:
        resp = ping(host, timeout=2)
        '''if resp == None:
            print(name, "(", host, ") ->  Not connected")
            return False
        elif resp == False:
            print(name, "(", host, ") -> Not valid IP")
            return False
        else:
            print(name, "(", host, ") ->  connected")
            return True
        '''
        if resp != None and resp != False:
            print(name, "(", host, ") ->  connected")
            return True
    except:
        None

with open('pingeador.json', 'r') as f:
    data = json.load(f)

threads=list()
'''
for i in data["pingeador"]:
    
    ip = data["pingeador"][i]["ip"]
    name = data["pingeador"][i]["name"]
    x=threading.Thread(name=name, target=myping, args=(ip, name,))
    threads.append(x)
    x.start()
  #  myping(ip, name)
'''
base = "192.168.1."
for j in range(256):
    ip = base+str(j+1)
    name=ip
    x=threading.Thread(target=myping, args=(ip, name,))
    threads.append(x)
    x.start()
