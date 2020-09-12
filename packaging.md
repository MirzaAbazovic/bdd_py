# Packaging in python

## Creating and installing package

Create folders and files structure that will hold code and depict structure of your package.

In each folder add ```__init__.py``` which is required if you want to import the directory as a package.
```__init__.py``` it is invoked when the package or a module in the package is imported and can be used to do some setup.
```__init__.py``` can also be used to automatically import the modules from a package.

We will leave it blank. 

```

├── common4bdd //this is name of package
│       ├── functions  //this is name of module
│       │       ├── __init__.py
│       │       └── web_common.py //code in module functions
│       └── steps //this is name of module
│           ├── __init__.py
│           └── steps_common.py //code in module steps
│       ├── __init__.py
│       ├── setup.py

```
Above is example of folder structure of package ```common4bdd```
It contains sub folders ```functions``` and ```steps``` with code in ```web_common.py``` and ```steps_common.py```
Every folder (including root ```common4bdd```) contains ```__init.py__```

In files ```web_common.py``` and ```steps_common.py``` You write code of your package in this case it will be code related with selenium manipulation and behave.

Ensure pip, setuptools, and wheel are up to date.

```python -m pip install --upgrade pip setuptools wheel```

```setup.py``` is the build script for [setuptools](https://pypi.org/project/setuptools/). 

It tells setuptools about your package (such as the name and version) as well as which code files to include.

```python
#setup.py file
from setuptools import setup, find_packages

setup(name='common4bdd',#You can use any name but usually top folder name
      version='1.0',
      description='Common stuff for Python BDD tests',
      author='Mirza Abazovic',
      author_email='mirza.abazovic@gmail.com',
      packages=find_packages()
      )

``` 

Fo more details go [here](https://packaging.python.org/tutorials/packaging-projects/)

To install package run

```bash
python setup.py install
``` 

During development of package (a lot of changes in source) use 

```bash
python setup.py develop
``` 

The develop will not install the package but it will create a .egg-link in the deployment directory back to the project source code directory.

Other option for installing is:

```pip install .```

and for development:

```pip install -e .```

## Importing modules

```import <module_name>```

Will import all from module and creates a separate namespace.
To invoke use ```<imported_namespace>.<module_name>.<function>```

```python
import steps
steps.steps_common.go_to_url(context, site)
```
To inspect what is in  module use ```dir(<module_name>)```

Individual objects from the module can be imported
```from <module_name> import <name(s)>```

Objects are imported into the caller’s symbol table.
The individual objects are directly accessible to the caller (no need .

```python
from steps import steps_common
steps_common.go_to_url(context, site)
```

To import all from module

```from <module_names> import *```

This places all the names of objects into the local symbol table:
- With the exception of any that begin with an underscore
- **NOTE: This isn’t necessarily recommended**
- Unless you know all the names will not conflict and overwrite existing names

Individual objects can be imported with alternate names
```from <module_name> import <name> as <alt_name>```

Good for avoiding conflicts with existing names.

Import the entire module under an alternate name
```import <module_name> as <alt_name>```

Used to create shorter name.