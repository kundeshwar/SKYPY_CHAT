from skpy import Skype


#you also from group 
slogin = Skype("kundeshwar15000@gmail.com","Kundeshwar15@")
contact = slogin.contacts["live:.cid"]
contact.chat.sendMsg("hello bhai")


#for i in contact:
#    print(i)


