"""
Acts as a way to define attributes about the package
"""

from setuptools import setup

setup(
#name for the package
name = 'example',

#current version of the package
version = '0.0.1',

#Your information
author='example',
author_email='example@example.com',

#specify the packages included. 
#Every folder with an __init__.py file is considered a package
packages=['example'],

#short and long descriptions(you can open() 
#then read() them from text files then pass them in)
description=open("short.txt","r").read(),
long_description=open("readme.txt","r").read(),

#url for the project
url='https://github.com/blah/example',

#put your license type here
license='license',

#this information is for categorizing the package on PyPi
#I took this section from python.org
classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    #more ways of describing or classifying your project (space separated)
    keywords='package setup keyword',

    #This section specifies the dependencies the package needs
    #these will install when someone runs "pip install <package>"
    install_requires=['django', 'numpy', 'sklearn'],

    #specifies what versions of python the package can run on
    #this means that the package currently supports versions from 2.7 to 3.6
    python_requires='>=2.7, <4',

    #specifies to include all of the files in the directory
    include_package_data=True,

    #here's where the functionality you want is
    #entry_points provides a way for users to access a function of your package
    #console_scripts specifies that it's a command line tool
    #In this example, the sample command calls the main function of __main__.py
    entry_points={
        'console_scripts': [
            'sample=example.sample:main'
        ],
    },
)