from setuptools import find_packages,setup
from typing import List 

def get_requirements(file_path:str) ->List[str]:
    ''' 
        this function will return list of requirements needed 
    '''
    hypen_e_dot = '-e .'
    requirement = []
    with open(file_path) as file_obj:
        requirement= file_obj.readlines()
        requirement=[req.strip() for req in requirement]
        
        if hypen_e_dot in requirement:
            requirement.remove(hypen_e_dot)
    return requirement


setup(
name='MLProjects',
version='0.0.1',
author='Karthik',
packages=find_packages(where="src"),     # 🔥 important
package_dir={"": "src"},                 # 🔥 important
install_requires=get_requirements('requirements.txt')

)