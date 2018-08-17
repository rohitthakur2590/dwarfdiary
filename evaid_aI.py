from evaid_utility import InitEvaid, Validate, Authorize, CreateNotes, DisplayLogInfo

#Initialize  Evaid
path = InitEvaid()
#Ask User for the password
password = Validate()
#Authorize the user
Authorize(password, path)
#Display log info
DisplayLogInfo()
#Ask user
CreateNotes(path)

