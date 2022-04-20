README
# Setting up the development environment
Packaged within this repo is a 'requirements.txt' file. This file contains all of the dependencies for this project. We will be using a virtual environment to develop.
## Setting up the virtual environment
1. Run this command: `python -m venv .venv`. This will create a virtual environment called '.venv' for you to develop inside. This venv prevents any dependencies we install from being a problem globally.
2. We now have to activate the script with this: `.venv/Scripts/Activate.ps1`.
3. Now that the script is activated, install the dependencies like so: `pip install -r requirements.txt`.
You should be all done! 
Many environments allow you to automatically activate the venv so you don't have to do it manually every time, maybe look into that.
## Creating the MySQL Server
1. Follow [this tutorial](https://realpython.com/python-mysql/) on how to download and set up the MySQL server locally on your device. 
2. Our machines have everything installed using the default settings, so if you change any port numbers you will have to make sure to change the port that Flashify is looking for in `database_API.py`.
3. We set our credentials as user: 'root', and pass: 'flashify'. **Please do not keep these default credentials**. Create your own secure username and password, store them with proper cryptographic techniques (e.g. hashing), and update `database_API.py` to use the new credentials.
4. You can also change the name of the created database quite easily in `database_API.py`, feel free to do so if you are inclined. 
### Using a Remote Database
Using a remote database with this project would be simple. We chose not to do so for this project due to cost concerns, but all that would have to be done is update the `connection` variable in `database_API.py` to the location and credentials used for the remote database, and the project will work. 
# Code Style Guidelines
## Formatting
We use `black` to format our code automatically. More documentation about that can be [found here](https://black.readthedocs.io/en/stable/the_black_code_style/index.html).
## Naming Conventions
We try to stick with `snake_case` but `camelCase` is also acceptable.
Please keep variable and functions names concise, unique, and descriptive. This will allow us to maintain a legible and welcoming code-base.
# Logins and API keys
This project should only require one login for the MySQL server, and no API keys. The login credentials are [discussed here](#creating-the-mysql-server) at the third bullet point. 
