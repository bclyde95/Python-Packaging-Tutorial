==========================
  Python package tutorial
==========================

This tutorial covers not only making a package but also making a script executable without calling python example.py. Just as you were interested in. It is in Python 3 but 2.7 is the same process with minor tweaks.

Directory structure:
->example
	setup.py
	license.txt
	manifest.in
	readme.txt
	short.txt
	->example
		__init__.py
		example.py
		file.csv
		printcsv.py
		sample.py

	FILES:
-----------------------

setup.py:
---------
This is the most important file for creating a package. It defines the attributes and requirements the package has. setup.py goes into detail on what each attribute does

restructure.txt:
----------
I have provided an example of the restructured text format so that you can get a good idea of how to create one of your own

manifest.in:
------------
This makes sure all .txt files are included

license.txt:
------------
Where all the information about your licensing goes

short.txt:
----------
Just an example of plugging in a text file for the description attribute

example/__init__.py:
------------
An empty file that signifies the directory as a package

example/example.py:
-------------------
The main file for running the "python example.py" way

example/printcsv.py:
--------------------
Contains the Prints class which houses the functionality of the package


example/sample.py:
------------------
This is the command line tool as specified in setup.py. It uses the example package to perform it's functionality.

file.csv:
---------
A simple two entry csv file to print out


PACKAGING PROCESS:
-------------------

Once every your setup file has been completed for your application and the your application is in working order. You can begin the packaging process.

1) In the package directory (the outer 'example' directory), run the 'python setup.py sdist'
   command.

2) After 'sdist' has been run, navigate to the new directory 'dist'

3) Copy the file path for the .tar.gz file and run a pip install with the file path as your 
   package. 'pip install C:\Users\bclyd\Documents\Examp\example\dist\example-0.0.1.tar.gz'

4) open python in the terminal and 'import example' to make sure it installed correctly

5) run 'sample file.csv' to test the command line tool

6) Congratulations, you now know how to create a python package