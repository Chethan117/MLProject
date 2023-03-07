from setuptools import find_packages, setup
from typing import List

'''
The value -e . is a command-line option used with pip to install a Python package in "editable" mode,
meaning the package is installed as a symbolic link to the package source code.

'''
HYPHEN_E_DOT='-e .'
'''
The get_requirements function is used to read and filter the list of package requirements from a file, 
ensuring that the -e . option is removed from the list if it is present. 
This makes it easier to distribute the package to others without including development-specific requirements.

'''
def get_requirements(file_path:str)->List[str]:

    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
name='MLProject',
version='0.0.1',
author='Chethan',
author_email='chethankb11@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
    )