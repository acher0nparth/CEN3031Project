README
# Setting up the development environment
Packaged within this repo is a 'requirements.txt' file. This file contains all of the dependencies for this project. We will be using a virtual environment to develop.
## Setting up the virtual environment
1. Run this command: `python -m venv .venv`. This will create a virtual environment called '.venv' for you to develop inside. This venv prevents any dependencies we install from being a problem globally.
2. We now have to activate the script with this: `.venv/Scripts/Activate.ps1`.
3. Now that the script is activated, install the dependencies like so: `pip -r requirements.txt`.
You should be all done! 
Many environments allow you to automatically activate the venv so you don't have to do it manually every time, maybe look into that.
