import urllib2
from Tkinter import *
import cookielib
from getpass import getpass
import sys
import os
from stat import *

root = Tk(className ="My first GUI")

message1 = Label(root,text="Enter text:")
message1.pack()
message = StringVar()
w = Entry(root,textvariable=message)
w.pack()
number1 = Label(root,text="Enter number:")
number1.pack()
number = StringVar()

#number.pack()
#message1 = Label(root,text="Enter text:")
#message1.pack()
#message = raw_input("Enter text: ")
#number = raw_input("Enter number: ")
#print(1)

x = Entry(root,textvariable=number)

x.pack()
def act():
	global cookielib
	global urllib2
	global number
	global message
	if __name__ == "__main__":  
	
   
    		username = "9676368424"
    		passwd = "dheeraj123"
	
    		#message = "+".join(str(message).split(' '))

 		#logging into the sms site
    		url ='http://site24.way2sms.com/Login1.action?'
    		data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

 		#For cookies

    		cj= cookielib.CookieJar()
    		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	
 	#Adding header details
    		opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
    		try:
    			#print(str(number))
        		usock =opener.open(url, data)
    		except IOError:
        		print "error1"
        		#return()
    		#print(999) 
    		jession_id =str(cj).split('~')[1].split(' ')[0]
    		send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    		send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+str(number.get())+'&message='+str(message.get())+'&msgLen=136'
    		opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
    
    
    		try:	
    			#print(number.get())
        		sms_sent_page = opener.open(send_sms_url,send_sms_data)
        	except IOError:
        		print "error2"
        	print "success" 		 
foo = Button(root,text="Send", command=act)
foo.pack()
root.mainloop()    		
        
    
        #return()
	
    
    #return ()
   
