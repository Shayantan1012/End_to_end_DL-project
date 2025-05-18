from setuptools import setup,find_packages
from typing import List
HYPEN_E_DOT = '-e .'

def get_requirement(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirement_list = []
    with open(file_path) as file_obj:
        requirement_list =file_obj.readlines()
        requirement_list = [req.replace('\n','') for req in requirement_list]
        
        if HYPEN_E_DOT in requirement_list:
            requirement_list.remove(HYPEN_E_DOT)
    return requirement_list

setup(

name="Xray",
version="0.0.1",
author="Shayantan Biswas",
author_email="shayantanbiswas137@gmail.com",
install_requires=get_requirement(r"C:\Users\SHAYANTAN BISWAS\Desktop\DeepLearningProject\requirements_dev.txt"),
packages=find_packages(include=["Xray*"])
)
    
