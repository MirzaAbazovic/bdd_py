# Demo tests of IB portal

https://portal.infobip.com

Create folders for common functions(classes) and steps. 

Add ```__init__.py``` in every folder and i root also.

Create setup.py on root folder
```python
from setuptools import setup

setup(name='IB Portal BDD',
      version='1.0',
      description='Python BDD tests for https://portal.infobip.com/',
      author='Mirza Abazovic',
      author_email='mirza.abazovic@gmail.com',
      packages=['BDDCommon',
                'BDDCommon.BDDCommonFunc',
                'BDDCommon.BDDCommonSteps', ]
      )

```

When You have a lot of changes (development) run :

```sudo python setup.py develop``` 

install it: 

```sudo python setup.py install ```

