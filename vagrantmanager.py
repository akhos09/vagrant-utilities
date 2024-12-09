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
            act = 'python.exe -m pip install --upgrade pip'
            install = 'pip install pick'
            print('Updating pip...')
            act_command = subprocess.getoutput(f"{act}")
            print(act_command)
            print ('-----------------------------')
            print('Installing the module pick...')
            installpick_command = subprocess.getoutput(f"{install}")
            print(installpick_command)
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
        '5) See all the options for plugins of your Vagrant environment': plugins,
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
    command_status = 'vagrant global-status'
    print('Showing all the machines of the system...')
    output = subprocess.getoutput(f"{command_status}")
    print(output)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def delete():
    status()
    print('------------------------------------------------')
    id_name_machine = (input('ID of the machine to be deleted: '))
    output = subprocess.getoutput(f"vagrant destroy {id_name_machine} -f")
    print(output)
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
    for path in execute("vagrant up"):
        print(path, end="")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def package():
    subprocess.run(["powershell", "-command", "cls"])
    print('--------------------------------------------------------------------------------------------------------------------------------')
    box = str(input('Please enter the name (name in the VB GUI) of the VM (Only VirtualBox) you want to package as a .box: '))
    print('--------------------------------------------------------------------------------------------------------------------------------')
    name = str(input('Enter the name of the new packaged box (without the .box format): '))
    for path in execute(f"vagrant package --base {box} --output {name}.box"):
        print(path, end="")
def plugins():
    print('test')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def execute(cmd): #CREDIT TO tokland https://stackoverflow.com/questions/4417546/constantly-print-subprocess-output-while-process-is-running, ty a lot
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
check()