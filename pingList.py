import subprocess
import os
with open('iplist.txt', 'r') as f:
    for ip in f:
        result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2",    ip],stdout=f, stderr=f).wait()
        if result:
                print(ip, "inactive")
                inactive = open('inactiveIP.txt','a+')
                inactive.write(ip)
                inactive.close()
        else:
                print(ip, "active")
                active = open('activeIP.txt','a+')
                active.write(ip)
                active.close()
