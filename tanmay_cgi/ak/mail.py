#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
print()
form = cgi.FieldStorage()
b1 = form.getvalue('username')
b2 = form.getvalue('password')
b3 = form.getvalue('recipient')
b4 = form.getvalue('subject')
b5 = form.getvalue('message')
print(b1)
print(b3)
print(b4)
print(b5)
f1 = open("maildata.yml",'w')
f1.write("username: %s\n"%(b1))
f1.close()
f1 = open("maildata.yml",'a')
f1.write("password: %s\n"%(b2))
f1.close()
f1 = open("maildata.yml",'a')
f1.write("recipient: %s\n"%(b3))
f1.close()
f1 = open("maildata.yml",'a')
f1.write("subject: %s\n"%(b4))
f1.close()
f1 = open("maildata.yml",'a')
f1.write("message: %s\n"%(b5))
f1.close()
print("<u>sending mail</u>")
x = sp.getstatusoutput("sudo ansible-playbook mail.yml")
#print(x)
print("Mail sent successfully.")