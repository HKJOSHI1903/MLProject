from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    ''' this functions returns the requiremts list'''
    HYPHENDOTE='-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if HYPHENDOTE in requirements:
            requirements.remove(HYPHENDOTE)
    return requirements

        
setup(
    name='mlproject',
    version='0.0.1',
    author='Harshit Joshi',
    author_email='Harshitjoshi769@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)