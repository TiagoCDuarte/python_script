#!/bin/python

#to-do
#add README
#add coments explaining the code
#add parameters to the function of option 6 to include the 7 inside it and calling with flags
#add option to filter more status codes and distinguish them by colour
#add option to set the speed of the requests (ex 10requests/s, 5 requests/s, 1 request/s)
#add the the option to the same but for sub domains.
#add another option to run for subdomains and dirs automatically
#add the option to export results to a file to be saved to later
#add option to grab the source code and filtrate links, images (to catch the paths), anything that is commented that can be usefull, (...) and also store it on a file

#######
import time
import os
import requests

Filename=""

#Functions
def wordlist():
    with open("names.txt", 'r') as file:
        for name in file:
            print(name.strip())

def add_name(): 
    with open("names.txt", 'a') as file: 
        word = input("Enter a word to add: ") 
        file.write("\n" + word)

def add_name_top():
#To be used in a scenario where we found a key word and we want to use it in the beggining of our wordlist
    with open("names.txt", 'r') as file: 
        old_list = file.read()
        #print(old_list)
        new_word = input("Enter a word to add: ") 
        appended_at_the_top = new_word + "\n" + old_list

    with open("names.txt", 'w') as file:
        file.write(appended_at_the_top)

def dir_finder(): 
    url = input("What is the target URL? (Please also add the http or https):") 
    with open("names.txt", 'r') as file: 
        for name in file:
            name = name.strip()
            testurl = url + "/" + name
            response = requests.get(testurl)
            #if response.status_code == 200:
            print(testurl+str(response))

def dir_finder2(): 
    url = input("What is the target URL? (Please also add the http or https):") 
    with open("names.txt", 'r') as file: 
        for name in file:
            name = name.strip()
            testurl = url + "/" + name
            response = requests.get(testurl)
            if response.status_code == 200:
                print(testurl+str(response))


def menu():
    option1 = "1-Read and display names"
    option2 = "2-Add a new name"
    option3 = "3-Exit"
    option4 = "4-Install requests"
    option5 = "5-Append word on top"
    option6 = "6-Run wordlist on target URL to find directories"
    option7 = "7-Same as 6 but shows only 200 codes"
    show_menu= True
    menu_attempts = 0

    while show_menu != False:
        print(option1)
        print(option2)
        print(option3)
        print(option4)
        print(option5)
        print(option6)
        print(option7)

        show_menu = input("Select an option: ")

        if show_menu == "1":
            print("Option 1 has been selected")
            wordlist()
            time.sleep(1)
        elif show_menu == "2":
            print("Option 2 has been selected")
            add_name()
            time.sleep(1)
        elif show_menu == "4":
            print("Option 4 has been selected")
            os.system("pip install requests")
            time.sleep(1)
        elif show_menu == "5":
            print("Option 5 has been selected")
            add_name_top()
            time.sleep(1)
        elif show_menu == "6":
            print("Option 6 has been selected")
            dir_finder()
            time.sleep(1)
        elif show_menu == "7":
            print("Option 7 has been selected")
            dir_finder2()
            time.sleep(1)
        elif show_menu == "3":
            print("Option 3 has been selected")
            show_menu = False
        else:
            print("Invalid option. Please try again.")
            menu_attempts+=1
            #print(menu_attempts)
            if menu_attempts == 3:
                print("You have select 3 times invalid options. This program will now close.")
                show_menu = False
                time.sleep(1)
        
#Code

menu ()
