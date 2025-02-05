import os
import sys
import subprocess
from contextlib import contextmanager
from pick import pick
import tkinter
from tkinter import filedialog as fd
from tkinter import Tk

#Method stay stay into the app's directory (for the future akhos09)
@contextmanager
def change_directory(target_dir):
    current_dir = os.getcwd()
    os.chdir(target_dir)
    try:
        yield
    finally:
        os.chdir(current_dir)


#Defined methods for VMs (status,create,delete,pack)(subproccess)---------------------------------------------------------------------------------------------------
class VagrantMachines:
    def machines_status(self): #Status--------------------------------------
        try:
            print("Showing all the machines of the system...")
            subprocess.run("vagrant global-status", check=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Error listing Vagrant machines: {e}")

    def create_machine(self): #Create(tk window to select the folder)--------------------------------------
        def select_file(): #Folder selector with tk
            counter = 3 #Counter made just in case none directory is selected.
            while counter >= 0:
                try:
                    print(
                        "Please select the directory where the Vagrantfile is located:\n"
                    )
                    root = tkinter.Tk()
                    root.withdraw()
                    root.wm_attributes("-topmost", 1)
                    folder_selected = fd.askdirectory()
                    root.destroy()

                    if not folder_selected:
                        print(
                            "Error: No directory selected. Please select a valid directory.\n"
                        )
                        counter = counter - 1
                        continue

                    if not os.path.exists(folder_selected):
                        print(
                            f"Error: Selected directory does not exist: {folder_selected}\n"
                        )
                        continue

                    return folder_selected
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

        folder_selected = select_file()

        try: #To go back to the script's folder after executing the command.
            with change_directory(folder_selected):
                subprocess.run("vagrant up", text=True)

        except subprocess.CalledProcessError as e:
            print(f"Error deploying the Vagrant machine: {e}")
            print("Ensure the selected directory contains a valid Vagrantfile.")

    def delete_machine(self): #Delete-----------------------------------------------
        self.machines_status()
        try:
            print("-" * 48)
            id_vm = input("ID of the machine you want to delete: ")
            subprocess.run(f"vagrant destroy {id_vm} -f", text=True)

        except subprocess.CalledProcessError as e:
            print(f"Error deleting the Vagrant machine: {e}")

    def pack_machine(self): #Pack--------------------------------------------------
        try:
            print("-" * 130)
            vm_name = input("Please enter the name (name in the VB GUI) of the VM (Only VirtualBox) you want to package as a .box: ").strip()
            if not vm_name:
                print("Error: You must enter a valid VirtualBox VM name.")
                return self.pack_machine()

            print("-" * 130)
            outputbox_name = input("Enter the name of the new box (without the .box format): ").strip()
            if not outputbox_name:
                print("Error: You must enter a valid name for the .box file.")
                return self.pack_machine()

            command = f"vagrant package --base {vm_name} --output {outputbox_name}.box"
            subprocess.run(command, text=True, shell=True, check=True)
            print(f"Successfully created {outputbox_name}.box (If the VM wasn't created before, it won't create the .box file.)")

        except subprocess.CalledProcessError as e:
            print("Error: Failed to package the VM. Check if the VirtualBox VM exists.")
            print(f"Details: {e.stderr}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


#Defined methods for plugins (list,install,uninstall,update,repair)(subproccess)---------------------------------------------------------------------------------------------------
class VagrantPlugins:
    def list_plugins(self): #List--------------------------------------------
        print("Showing all the plugins installed on the system...")
        try:
            subprocess.run("vagrant plugin list", text=True)

        except subprocess.CalledProcessError as e:
            print(f"Error listing plugins of your Vagrant environment: {e}")

    def install_plugin(self): #Install--------------------------------------------
        plugin = str(input("Enter the name of the plugin you want to install: "))
        try:
            subprocess.run(f"vagrant plugin install {plugin}", text=True)

        except subprocess.CalledProcessError as e:
            print(f"Error installing the plugin: {e}")

    def uninstall_plugin(self): #Uninstall--------------------------------------------
        plugin = str(input("Enter the name of the plugin you want to uninstall: "))
        try:
            subprocess.run(f"vagrant plugin uninstall {plugin}", text=True)

        except subprocess.CalledProcessError as e:
            print(f"Error uninstalling the plugin: {e}")

    def update_plugin(self): #Update--------------------------------------------
        plugin = str(input("Enter the name of the plugin you want to update: "))
        try:
            subprocess.run(f"vagrant plugin update {plugin}", text=True)

        except subprocess.CalledProcessError as e:
            print(f"Error updating the plugin: {e}")

    def repair_plugin(self): #Repair--------------------------------------------
        plugin = str(input("Enter the name of the plugin you want to repair: "))
        try:
            subprocess.run(f"vagrant plugin install {plugin}", text=True)

        except subprocess.CalledProcessError as e:
            print(f"Error repairing the plugin: {e}")


class Menus: #Defined the two menus for the app (module pick)-------------------------------
    def __init__(self): #Instance the two classes
        self.vagrant_machines = VagrantMachines()
        self.vagrant_plugins = VagrantPlugins()

    def prompt_exit(self): #Selector to stay in the app------------------------------------
        option = input("Do you want to exit the script? (y/n): ").strip().lower()
        if option == "n":
            self.main_menu()
        else:
            print("Exiting...")
            sys.exit()

    def main_menu(self): #Main menu--------------------------------------------------------
        while True:
            title = "----Management script for Vagrant (Use ↑↓ and ENTER)---- @akhos09"
            options = [
                "1) List all the Vagrant machines",
                "2) Create a Vagrant machine using a Vagrantfile",
                "3) Delete a Vagrant machine (using the id)",
                "4) Pack a virtual machine from VirtualBox as a box",
                "5) See all the options for the plugins of your Vagrant environment",
                "6) Exit",
            ]

            option, _ = pick(options, title, indicator="=>", default_index=0)
            actions = {
                "1) List all the Vagrant machines": self.vagrant_machines.machines_status,
                "2) Create a Vagrant machine using a Vagrantfile": self.vagrant_machines.create_machine,
                "3) Delete a Vagrant machine (using the id)": self.vagrant_machines.delete_machine,
                "4) Pack a virtual machine from VirtualBox as a box": self.vagrant_machines.pack_machine,
                "5) See all the options for the plugins of your Vagrant environment": self.plugins_menu,
                "6) Exit": sys.exit,
            }

            action = actions.get(option)
            if action:
                action()
                self.prompt_exit()
            else:
                print("Please select a correct option.")

    def plugins_menu(self): #Plugins menu--------------------------------------------------------
        while True:
            title = "----Options for plugins (Use ↑↓ and ENTER)----"
            options = [
                "1) List all the plugins installed",
                "2) Install a plugin",
                "3) Uninstall a plugin",
                "4) Update a plugin",
                "5) Repair a plugin",
                "6) Go back to the main menu",
                "7) Exit",
            ]

            option, _ = pick(options, title, indicator="=>", default_index=0)
            actions = {
                "1) List all the plugins installed": self.vagrant_plugins.list_plugins,
                "2) Install a plugin": self.vagrant_plugins.install_plugin,
                "3) Uninstall a plugin": self.vagrant_plugins.uninstall_plugin,
                "4) Update a plugin": self.vagrant_plugins.update_plugin,
                "5) Repair a plugin": self.vagrant_plugins.repair_plugin,
                "6) Go back to the main menu": self.main_menu,
                "7) Exit": sys.exit,
            }

            action = actions.get(option)
            if action:
                action()
                self.prompt_exit()
            else:
                print("Please select a correct option.")


def main(): #Main function of the code (check if pick is installed)-------------------------------------
    try:
        import pick
        app_menu = Menus()
        app_menu.main_menu()

    except ImportError as e:
        print(
            """
              Pick module (needed for the menu) not installed. Please install the module (with pip) and execute the app again.
            """
        )

if __name__ == "__main__":
    main()