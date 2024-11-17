# Vagrant Utilities

A collection of configuration files and a script that are used with Vagrant.

## Table of Contents
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Dependencies

The script and the config files requires the following libraries and tools:
1.- **Virtual Box**: Hypervisor used for the creation of the VMs.

2. **Vagrant**: Obviously needed for all of this. 

3. **os**: A module needed to change the working path.

4. **subproccess**: A module to run the powershell commands of Vagramt.

5. **Tkinter**: For the file dialog to select `.wav` files.

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/akhos09/vagrant-utilities
   cd vagrant-utilities
   ```

## Usage

1. **Run the script**:

   Open a terminal or command prompt and navigate to the directory containing the script. Run the following command:

   ```
   python vagrantmanager.py
   ```

2. **Import the Vagrant file**

   Select the Vagrantfile using the second option of the script.

## Troubleshooting
- Make sure that `Python` and `Vagrant` are installed and updated.
  
## License

See the [LICENSE](LICENSE) file for details.
