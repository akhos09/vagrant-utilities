# SCRIPT VAGRANT PYTHON MANAGEMENT
import os
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
    
print('----Welcome to the managment script for Vagrant----')
print('1) List all the Vagrant machines')
print('2) Create a Vagrant machine using a Vagrantfile')
print('3) Delete a Vagrant machine (using the id)')
print('4) Exit')
print('---------------------------------------------------')

option = int(input('Select an option (1-4): '))
while option != 4:
    if option != range(1,4):
        print('Please execute again the script and select a correct option. (1-4)')
        break
    elif option == 1:
            status()
    elif option == 2:
            create()
    elif option == 3:
                delete()
else:
    print('Exiting...')
