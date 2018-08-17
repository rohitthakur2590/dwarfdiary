import re
import os
import datetime
import time
command_1 = "close it evaid"
command_2 = "show detail evaid"
command_3 = "show contents evaid"
command_4 = "show options evaid"
def InitEvaid():
    path_name = "evaid"
    if not os.path.isdir(path_name):
        print("Booting Evaid 1.0  For the First Time ...")
        os.mkdir(path_name, 755)
        print("Init Process Completed")
    return path_name
def Validate():
    while True:
        password = input("Enter a password: ")
        if len(password) < 8:
            print("Minimum Length is  8 letters")
        elif re.search('[0-9]',password) is None:
            print("At least one Numeric required")
        elif re.search('[A-Z]',password) is None:
            print("At least one capital letter required")
        else:
            return password

def Authorize(password, path):
    pwd_file_name = path + "/pwd.txt"
    if os.path.exists(pwd_file_name):
        if password in open(pwd_file_name).read():
            print("Welcome Rohit")
        else:
            print('Sorry Wrong Password')
    else:
        pwd_file = open(pwd_file_name, "w")
        pwd_file.write("password =" + password)
        pwd_file.close()

def CreateNotes(path):
    # Create a file with date name
    today_note = time.strftime("%d-%m-%Y")
    today_note += ".txt"
    file_name = path + "/" + today_note
    # open the file
    my_file = open(file_name, "a+")

    print("Start Writing ...")
    while True:
        data = input()
        command = EvaidCommandProcess(data, path)
        if command == "close it evaid":
                break
        if data != command:
            data += '\n'
            my_file.write(data)
        pass
    my_file.close()

def DisplayLogInfo():
    # get date
    ## dd/mm/yyyy format
    current_date = datetime.datetime.now()
    print('Day: ', current_date.strftime('%A'))
    today_note = time.strftime("%d-%m-%Y")
    print('Time: ', time.strftime("%H:%M:%S", time.gmtime()))
    print('Date: ', today_note)

def EvaidCommandProcess(data, path):
    command = ''
    if data == command_3:
        file = open(path, "r")
        for line in file:
            print(line)
        command = command_3
    elif data == command_1:
        command = command_1
        print("Good Bye..")
    elif data == command_2:
        DisplayLogInfo()
        command = command_2
    elif data == command_4:
        print(command_1)
        print(command_2)
        print(command_3)
        print(command_4)
        command = command_4
    else:
        command = ""
    return command