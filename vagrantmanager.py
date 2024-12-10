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
    '5) See all the options for the plugins of your Vagrant environment',
    '6) Exit'
]
def clear():
    subprocess.run("cls", shell=True)
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
        clear()
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
        '5) See all the options for the plugins of your Vagrant environment': plugins,
        '6) Exit': sys.exit
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
    clear()
    print('Showing all the machines of the system...')
    subprocess.run("vagrant global-status",text=True)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def delete():
    clear()
    status()
    print('------------------------------------------------')
    id_name_machine = (input('ID of the machine to be deleted: '))
    subprocess.run(f"vagrant destroy {id_name_machine} -f",text=True)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def select_file():
    subprocess.run(["powershell", "-command", "cls"])
    print('Please select the directory where the Vagrantfile is located at:  ')
    root = tkinter.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    folder_selected = fd.askdirectory()
    root.destroy()
    return folder_selected
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def create():
    clear()
    folder_selected = select_file()
    os.chdir(f'{folder_selected}') 
    subprocess.run("vagrant up",text=True)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def package():
    clear()
    print('--------------------------------------------------------------------------------------------------------------------------------')
    box = str(input('Please enter the name (name in the VB GUI) of the VM (Only VirtualBox) you want to package as a .box: '))
    print('--------------------------------------------------------------------------------------------------------------------------------')
    name = str(input('Enter the name of the new packaged box (without the .box format): '))
    subprocess.run(f"vagrant package --base {box} --output {name}.box",text=True)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def plugins():
    def list():
        print('Showing all the plugins installed on the system...')
        subprocess.run('vagrant plugin list',text=True)
#-------------------------------------------------------------------
    def install():
        plugin = str(input('Enter the name of the plugin you want to install: '))
        subprocess.run(f'vagrant plugin install {plugin}',text=True)
#------------------------------------------------------------------
    def uninstall():
        plugin = str(input('Enter the name of the plugin you want to uninstall: '))
        subprocess.run(f'vagrant plugin uninstall {plugin}',text=True)
#------------------------------------------------------------------
    def update():
        plugin = str(input('Enter the name of the plugin you want to update: '))
        subprocess.run(f'vagrant plugin update {plugin}',text=True)
#------------------------------------------------------------------
    def repair():
        plugin = str(input('Enter the name of the plugin you want to repair: '))
        subprocess.run(f'vagrant plugin repair {plugin}',text=True)
#------------------------------------------------------------------
    clear()
    TITLE = '----Options for plugins (Use ↑↓ and ENTER)----'
    OPTIONS = [
    '1) List all the plugins installed',
    '2) Install a plugin',
    '3) Uninstall a plugin',
    '4) Update a plugin',
    '5) Repair a plugin',
    '6) Exit'
    ]
    option, _ = pick(OPTIONS, TITLE, indicator='=>', default_index=0)
    actions = {
        '1) List all the plugins installed': list,
        '2) Install a plugin': install,
        '3) Uninstall a plugin': uninstall,
        '4) Update a plugin': update,
        '5) Repair a plugin': repair,
        '6) Exit': sys.exit
    }
    action = actions.get(option)
    if action:
        action()
        if option != '6) Exit':
            prompt_exit()
    else:
        print('Please select a correct option.')
        case()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
check()
#made by @akhos09 github