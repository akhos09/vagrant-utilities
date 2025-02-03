# Vagrant Utilities

A collection of configuration files and a script designed to enhance Vagrant usage on Windows 11.

## Table of Contents

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Development](#development)
- [License](#license)

## Dependencies

Ensure the following tools and Python modules are installed:

1. **VirtualBox**: Hypervisor used for creating virtual machines.
2. **Vagrant**: Required for managing virtual environments.
3. **Python**: Ensure Python is installed and added to your system's PATH.
4. **Python Modules**:
   - **pick**: For menu selection.
   - **os**: To change the working directory.
   - **subprocess**: To execute PowerShell commands via Vagrant.
   - **tkinter**: For file dialog to select the directory containing the Vagrantfile.

## Installation

1. **Clone this repository**:

   ```bash
   git clone https://github.com/akhos09/vagrant-utilities.git
   cd vagrant-utilities
   ```

2. **Install required Python modules**:

   You can install the necessary modules using `pip`:

   ```bash
   pip install pick
   ```

   Note: `os`, `subprocess`, and `tkinter` are standard libraries included with Python.

## Usage

1. **Run the script**:

   Open a terminal or command prompt, navigate to the directory containing the script, and execute:

   ```bash
   python vagrantmanager.py
   ```

2. **Import the Vagrantfile**:

   Use the second option in the script to select and import the desired Vagrantfile.

3. **List all Vagrant machines**:

   Choose the first option in the script to display all existing Vagrant machines.

4. **Delete a Vagrant machine**:

   Select the second option in the script and enter the ID of the machine you wish to delete (as shown in the list from the first option).

5. **Package a machine into a box**:

   Use the "Package Machine" option to package an existing Vagrant machine into a reusable box file.

6. **Manage Plugins**:

   Use the "Plugin Manager" option to install, update, or remove Vagrant plugins easily from within the script.

## Troubleshooting

- Ensure that `Python`, `VirtualBox`, and `Vagrant` are installed and up to date.
- If a VM with the same name already exists, modify the name in the Vagrantfile or delete the existing VM to prevent conflicts.
- Remove unused network interfaces to avoid potential errors.
- If the installation stalls during the network interface renaming process (e.g., "eth1 renamed as enp0s8"), retry the operation. Persistent issues may indicate syntax errors in the Vagrantfile.
- If a VM's folder isn't deleted due to residual logs (often occurring when a VM is destroyed while running), manually delete the folder and attempt the operation again.

## Development

Planned features include:

- Linux support
- Making a .exe for the app.

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.