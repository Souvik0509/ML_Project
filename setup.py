from setuptools import find_packages,setup
from typing import List

def get_requirments(fle_pth:str)->List[str]:
    ''' 
     this  function will  return  list  of  our required packages 
    '''
    requirements = [] 
    not_required = '-e .'
    with open(fle_pth) as fle_obj:
        requirements = fle_obj.readlines()
        requirements = [req.replace("\n" ," ")  for req in requirements]

        if not_required in requirements:
            requirements.remove(not_required)

    return requirements

setup(
name = 'MLProject',
version = '0.0.1',
author = 'Souvik',
author_email= 'souviksarkar1000@gmail.com',
packages=find_packages(),
install_requires = get_requirments("requirement.txt")
)