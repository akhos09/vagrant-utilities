# SCRIPT VAGRANT PYTHON MANAGEMENT
import os
from pick import pick
import subprocess
import tkinter
from tkinter import filedialog as fd
from tkinter import Tk
    
def status():
    command = 'vagrant global-status'
    print('Showing all the machines of the system...')
    proc = subprocess.getoutput(["powershell", "-command", f"{command}"])
    print(proc)
    
def select_file():
    print('Please select the directory where the Vagrantfile is located at:  ')
    root = tkinter.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    folder_selected = fd.askdirectory()
    root.destroy()
    return folder_selected

def create():
    folder_selected = select_file()
    os.chdir(f'{folder_selected}')
    command = 'vagrant up'
    print('The installation of the machine will be running in the background. Please wait until it finishes...')
    proc = subprocess.getoutput(["powershell", "-command", f"{command}"])
    print(proc)

def delete():
    id_name_machine = (input('ID of the machine to be deleted: '))
    result = subprocess.getoutput(f"vagrant destroy {id_name_machine} -f")
    print(result)
    
def case():
    title = '----Managment script for Vagrant (Use ↑↓ and ENTER)---- @akhos09'
    options = ['1) List all the Vagrant machines', '2) Create a Vagrant machine using a Vagrantfile', '3) Delete a Vagrant machine (using the id)', '4) Exit']
    option, index = pick(options, title, indicator='=>', default_index=2)
    
    if option == '1) List all the Vagrant machines':
        status()
        yesno = str(input('Do you want to exit the script? (y/n): '))
        if yesno == 'n':
            case()
        else:
            print ('Exiting...')
            exit
    elif option == '2) Create a Vagrant machine using a Vagrantfile':
        create()
        yesno = str(input('Do you want to exit the script? (y/n): '))
        if yesno == 'n':
            case()
        else:
            print ('Exiting...')
            exit
    elif option == '3) Delete a Vagrant machine (using the id)':
        delete()
        yesno = str(input('Do you want to exit the script? (y/n): '))
        if yesno == 'n':
            case()
        else:
            print ('Exiting...')
            exit
    elif option == '4) Exit':
        print('Exiting...')
        exit
    else:
        print('Please select a correct option.')

case()
