from setuptools import find_packages,setup
'''
'Find Packages' also search for sub-models in our model
'Setup' for the versioning of our project
'''
from typing import List

HYPEN_E_DOT='-e .'
    
def get_requirements(file_path: str)->List[str]:
    requirements=[]
    
    with open(file_path) as file_obj:
        # Read lines from requirements.txt and strip the '\n' character
        # requirements = [req.strip() for req in file_obj.readlines()]
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

    # Remove all occurrences of HYPEN_E_DOT
    requirements = [req for req in requirements if req != HYPEN_E_DOT]

    return requirements

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Ankit',
    author_email='kadiyanankit11@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)