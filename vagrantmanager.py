# SCRIPT VAGRANT-MANAGEMENT
#V1.0
from __future__ import print_function
import os
from pick import pick
import subprocess
import tkinter
from tkinter import filedialog as fd
from tkinter import Tk
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
            print('Updating pip...')
            proc1 = subprocess.getoutput(["powershell", "-command", f"{act}"])
            print(proc1)
            command = 'pip install pick'
            print ('-----------------------------')
            print('Installing the module pick...')
            proc2 = subprocess.getoutput(["powershell", "-command", f"{command}"])
            print(proc2)
            print('Installation completed. Execute the script again with pick installed.')
        else:
            print('Exiting...')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
def case():
    title = '----Managment script for Vagrant (Use ↑↓ and ENTER)---- @akhos09'
    options = ['1) List all the Vagrant machines', '2) Create a Vagrant machine using a Vagrantfile', '3) Delete a Vagrant machine (using the id)', '4) Repack a virtual machine from VirtualBox','5) Exit']
    option, index = pick(options, title, indicator='=>', default_index=0)
    if option == '1) List all the Vagrant machines':
        status()
        yesno = str(input('Do you want to exit the script? (y/n): '))
        if yesno == 'n':
            subprocess.run("cls",shell=True)
            case()
        else:
            print ('Exiting...')
            exit
            
    elif option == '2) Create a Vagrant machine using a Vagrantfile':
        create()
        yesno = str(input('Do you want to exit the script? (y/n): '))
        if yesno == 'n':
            subprocess.run("cls",shell=True)
            case()
    elif option == '3) Delete a Vagrant machine (using the id)':
        delete()
        yesno = str(input('Do you want to exit the script? (y/n): '))
        if yesno == 'n':
            subprocess.run("cls",shell=True)
            case()
        else:
            print ('Exiting...')
            exit
    elif option == '4) Pack a virtual machine from VirtualBox as a box ':
        package()
        yesno = str(input('Do you want to exit the script? (y/n): '))
        if yesno == 'n':
            subprocess.run("cls",shell=True)
            case()
        else:
            print ('Exiting...')
            exit
    elif option == '5) Exit':
        print('Exiting...')
        exit
    else:
        print('Please select a correct option.')
        case()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
def status():
    command = 'vagrant global-status'
    print('Showing all the machines of the system...')
    proc = subprocess.getoutput(["powershell", "-command", f"{command}"])
    print(proc)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
def select_file():
    print('Please select the directory where the Vagrantfile is located at:  ')
    root = tkinter.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    folder_selected = fd.askdirectory()
    root.destroy()
    return folder_selected
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
def create():
    folder_selected = select_file()
    os.chdir(f'{folder_selected}') 
    for path in execute(["vagrant","up"]):
        print(path, end="")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
def delete():
    status()
    print('------------------------------------------------')
    id_name_machine = (input('ID of the machine to be deleted: '))
    result = subprocess.getoutput(f"vagrant destroy {id_name_machine} -f")
    print(result)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
def execute(cmd): #CREDIT TO tokland https://stackoverflow.com/questions/4417546/constantly-print-subprocess-output-while-process-is-running, ty a lot
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
def package():
    print('--------------------------------------------------------------------------------------------------------------------------------')
    box = str(input('Please enter the name (name in Vagrant NOT the name in the VB GUI) of the VM (Only VirtualBox) you want to package as a .box: '))
    name = str(input('Enter the name of the packaged box (without the .box format): '))
    for path in execute(["vagrant","package","--base",f"{box}","--output",f"{name}"]):
        print(path, end="")
check()
