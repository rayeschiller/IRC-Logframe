# Setup Instructions

### Virtualenv setup
Open Terminal and Install pip and run the following:

```sh
sudo apt-get install python-pip

sudo pip install virtualenv

mkdir ~/.virtualenvs

sudo pip install virtualenvwrapper

export WORKON_HOME=~/.virtualenvs

echo ". /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

source ~/.bashrc

mkvirtualenv IRC-logframe
```

### Directory setup
1. Create a new directory named __Sites__ on your home directory. `mkdir ~/Sites`
2. Cd into sites: `cd ~/Sites`
3. Within the _Sites_ directory create a new directory and name it _IRC-logframe_ then cd into it: 
   ```mkdir IRC-logframe```
   ```cd IRC-logframe```
4. Clone bitbucket repository in the command line using 
   ```git clone REPO_URL```
5. cd into the repo folder
6. Copy _.env.example_ and name it _.env_. Ex: `cp .env.example .env`
7. Install dependencies: `pip install -r requirements.txt`
8. Apply migrations: `python manage.py migrate`
9. Run server: `python manage.py runserver`
10. Go to _http://127.0.0.1:8000/_ to see the django app

### Frontend Setup
1. Install node version manager(nvm): `curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.6/install.sh | bash`. __Note__: You may need to install _curl_ `sudo apt-get install curl`.
2. Install node version 9.2. `nvm install 9.2.0`. Then switch to this version `nvm use 9.2.0`
3. CD into the frontend folder: `cd ~/Sites/IRC-logframe/<NAME_OF_CLONED_REPO>/frontend/IRC-logframe/`
4. Run `npm install`
5. Once all dependencies are installed you can start the angular app by running `npm run-script ng serve` within _frontend/IRC-logframe_ 
6. Test by opening you browser and going to http://localhost:4200.

# Database Configuration
By default, this application will use sqlite3 as a database backend. If a different backend is needed, please add the following to your _.env_ file. This example assumes you are using postgresql as a database backend:
```vim
DB_ENGINE=django.db.backends.postgresql
DB_NAME=nameofdb
DB_PASSWORD=passwordfordb
DB_USER=usernamefordb
DB_HOST=hostiporname
DB_PORT=portnumber
```

# Production
For production, please change or add the following to your _.env_ file:
```vim
ALLOWED_HOSTS=name.com,smeti.com,etc.com " A list of comma separated hostname (MUST BE CHANGED IN PROD. The use of * is discouraged.
SECRET_KEY=yoursecretkey " Do not use the one from .env.example as it may not be secure
```

# FAQ

__Why virtual environment?__
if you have more than one project or use Python on your machine for things other than Django, you may run into dependency issues between your applications and the installed packages. For this reason, we'll be using virtualenv to manage our Django installation. This is common, and recommended, practice among Python and Django users.

__How to activate virtual environment?__
Open a terminal window and type: workon IRC-logframe Your current terminal will use the python version used by the project’s virtualenv

__How to exit virtual environment?__
On the terminal type: deactivate or just close the terminal
