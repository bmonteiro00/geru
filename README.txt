README
==================

First version of the application challange.

Points to improve:
 -add ssl connection
 -write new more units tests
 -write functional tests (study how to do it)
 -refactor on key code points.
 -ignore unnecessary files in this repo
 -refactor on initialize_db.py, remove the hard-coded path to development.ini.

Getting Started
---------------

Install python.
Install pyramid.(pip install "pyramid==1.9.2")
Install pyramid_debugtoolbar. (pip install "pyramid_debugtoolbar")
Install pyramid_jinja2. (pip install "pyramid_jinja2")

Maybe on diferent enviromment is possible to install more dependecies.

There are two ways to run it :

In both cases you should change the path for development.ini. This step is important to initialize and create the database.

Change the path of the following commands in development.ini. Rename the path: "C:/Users/Bruno/PycharmProjects/GERU/development.ini" to desire one.
   -setup_logging("C:/Users/Bruno/PycharmProjects/GERU/development.ini")
   -settings = get_appsettings("C:/Users/Bruno/PycharmProjects/GERU/development.ini")
   

--------------------------------------------------------------------------------------------------------------------------------------------
Mode one : 
---------------------------

1 - Clone the entire repo. Open it in PyCharm Intellij professional version.

2 - Change the path of the following commands in development.ini. Rename the path: "C:/Users/Bruno/PycharmProjects/GERU/development.ini" to desire one.
   -setup_logging("C:/Users/Bruno/PycharmProjects/GERU/development.ini")
   -settings = get_appsettings("C:/Users/Bruno/PycharmProjects/GERU/development.ini")

3 - Run the application on PyCharm.


------------------------------------------------------------------------------------------------------------------------------------------

Mode two:
--------------------------
1 - Clone the entire repo.
2 - On the root of your cloned repo, execute "pserve development.ini". The application will start run.

