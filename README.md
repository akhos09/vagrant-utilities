
# Vagrant Utilities

A collection of configuration files and a script that are used with Vagrant on Windows 11.

## Table of Contents
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Dependencies

The script and the config files requires the following libraries and tools:

1. **Virtual Box**: Hypervisor used for the creation of the VMs.

2. **Vagrant**: Obviously needed for all of this.

3. **pick**: Module needed for the menu. 

4. **os**: A module needed to change the working path.

5. **subproccess**: A module to run the powershell commands of Vagramt.

6. **Tkinter**: For the file dialog to select the directory that contains the Vagrantfile.

## Installation

1.**Clone this repository:**

   ```
   git clone https://github.com/akhos09/vagrant-utilities
   cd vagrant-utilities
   ```

## Usage

1.**Install pick (or use the build-in function of the script that installs it)**

   ```
   pip install pick
   ```

2. **Run the script**:

   Open a terminal or command prompt and navigate to the directory containing the script. Run the following command:

   ```
   python vagrantmanager.py
   ```

3. **Import the Vagrant file**

   Select the Vagrantfile using the second option of the script.

4. **List all the vagrant machines**

   Use the first option of the script.

5. **Delete a vagrant machine**

    Use the second option of the script and enter the ID of the machine (the one shown in the first option)

## Troubleshooting

   - Make sure that `Python` and `Vagrant` are installed and updated.
   - If a VM already created has the same name as the one you want to create, change the name in the Vagrantfile or delete the VM with the same name. (This causes an error that doesn't let the creation of the new VM).
   - Delete the network interfaces that you don't use anymore. This causes a lot of errors than can be fixed only doing that.
   - If the installation gets stucked in the rename message (the one that says eth1 renamed as enp0s8 or something like that), try again. If it's getting still stucked check your Vagrantfile. This is caused because of bad syntax.
   - If the folder of the VM wasn't deleted was because of the folder Logs. This happens when the VM is destroyed (vagrant destroy command) while is running. Delete the folder and try again (This happens with the creation of new VMs with the same name of another that already existed).
  
## License

See the [LICENSE](LICENSE) file for details.

## Credits

For the ongoing output function made by the user tokland, ty a lot mate :) [StackOverflow](https://stackoverflow.com/questions/4417546/constantly-print-subprocess-output-while-process-is-running)

## Development

I'm planning to adding new features. An option to choose different Hypervisors (VMWare, HyperV, etc.), a repacker for VMs that you have, and a plugin manager.
