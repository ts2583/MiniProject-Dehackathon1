# MiniProject-Dehackathon1
Tech Stack:
Backend: Flask/Python (3.7)
Data/Database: SQL/sqlite will move to postgress

Piping Flask && Data?
SqlAlchemy works well

# How to run and install using Pycharm
After getting the project from a zip file,
make sure u open the project folder via pycharm.

After doing that, you'll need to be able to setup an virtualenv for the
project contents. 

Go to: File -> Settings -> Project: MiniProject-Dehackathon -> Project Interpreter
-> Click on the Gear Sign -> Add... -> Then and a new Virtualenv Environment.

Then on the section where terminal is located make sure the virtualenv is available
you'll see (MiniProject-Dehackathon1-master).

After that do this command on terminal install everything via pip
doing
pip install flask flask_sqlalchemy flask_marshmallow

# to run:
run on debug "python coffeeshop.py" on directory folder
or setup paths:

Windows:
 set FLASK_APP=coffeelibrary.py
 set FLASK_ENV=development
 
Linux:
  export FLASK_APP=coffeelibrary.py
  export FLASK_ENV=development

Then: flask run

note: make sure you're in the directory where coffeelibrary.py is located
