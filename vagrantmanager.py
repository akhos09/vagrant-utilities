# SCRIPT VAGRANT-MANAGEMENT
#V1.1
from __future__ import print_function
import os
import sys
from pick import pick
import subprocess
import tkinter
from tkinter import filedialog as fd
from tkinter import Tk
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
TITLE = '----Management script for Vagrant (Use ↑↓ and ENTER)---- @akhos09'
OPTIONS = [
    '1) List all the Vagrant machines',
    '2) Create a Vagrant machine using a Vagrantfile',
    '3) Delete a Vagrant machine (using the id)',
    '4) Pack a virtual machine from VirtualBox as a box',
    '5) Exit'
]
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def check():
    try:
        import pick
        case()
    except ImportError as e:
        print('---------------------------------------------------------------------')
        print('Module named "pick" not found. Please install pick (pip install pick)')
        print('---------------------------------------------------------------------')
        yesno = str(input('Do you want to install it? (y/n): '))
        if yesno == 'y':
            print('Updating pip...')
            subprocess.run("python.exe -m pip install --upgrade pip",text=True)
            print('-----------------------------')
            print('Installing the module pick...')
            subprocess.run("pip install pick",text=True)
            print('---------------------------------------------------------------------')
            print('Installation completed. Execute the script again with pick installed.')
        else:
            print('Exiting...')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def prompt_exit():
    option = input('Do you want to exit the script? (y/n): ').strip().lower()
    if option == 'n':
        subprocess.run("cls", shell=True)
        case()
    else:
        print('Exiting...')
        sys.exit()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def case():
    option, _ = pick(OPTIONS, TITLE, indicator='=>', default_index=0)
    actions = {
        '1) List all the Vagrant machines': status,
        '2) Create a Vagrant machine using a Vagrantfile': create,
        '3) Delete a Vagrant machine (using the id)': delete,
        '4) Pack a virtual machine from VirtualBox as a box': package,
        '5) Exit': sys.exit
    }
    action = actions.get(option)
    if action:
        action()
        if option != '5) Exit':
            prompt_exit()
    else:
        print('Please select a correct option.')
        case()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def status():
    print('Showing all the machines of the system...')
    subprocess.run("vagrant global-status",text=True)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def delete():
    status()
    print('------------------------------------------------')
    id_name_machine = (input('ID of the machine to be deleted: '))
    subprocess.run(f"vagrant destroy {id_name_machine} -f",text=True)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def select_file():
    print('Please select the directory where the Vagrantfile is located at:  ')
    root = tkinter.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    folder_selected = fd.askdirectory()
    root.destroy()
    return folder_selected
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def create():
    folder_selected = select_file()
    os.chdir(f'{folder_selected}') 
    subprocess.run("vagrant up",text=True)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def package():
    subprocess.run(["powershell", "-command", "cls"])
    print('--------------------------------------------------------------------------------------------------------------------------------')
    box = str(input('Please enter the name (name in the VB GUI) of the VM (Only VirtualBox) you want to package as a .box: '))
    print('--------------------------------------------------------------------------------------------------------------------------------')
    name = str(input('Enter the name of the new packaged box (without the .box format): '))
    subprocess.run(f"vagrant package --base {box} --output {name}.box",text=True)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
check()
#made by @akhos09 github