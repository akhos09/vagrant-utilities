# Vagrant Utilities

A collection of configuration files and a script that are used with Vagrant in Windows 11.

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
  
## License

See the [LICENSE](LICENSE) file for details.

## Credits

For the ongoing output funcion made by the user tokland, ty a lot mate :) [StackOverflow](https://stackoverflow.com/questions/4417546/constantly-print-subprocess-output-while-process-is-running)
