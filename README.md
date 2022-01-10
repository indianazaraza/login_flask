# README.md

Login made with css3 and html5 that runs on Flask. There is no password or user defined, so clicking the log in button takes you to the info view with a success message.

This was done on linux mint 20.

## How to run the environment

First, you **need** to install virtualenv. If you need to specify a version, go to the versions file.
~~~
pip3 install virtualenv==your_version
~~~

Then, from the login_flask folder, open a terminal and type the following command:
~~~
source env/bin/activate
~~~

To run the application: 
~~~
python3 app.py
~~~

By default the debug mode in the file is false, to change it, go to the last line of the app.py file:
~~~
app.run(debug=True)
~~~

## Folders

Inside the templates folder are the views: home(login), info(success message)

Inside the static folder there are other folders: styles(css files with the same names as the views), gallery(background images)


