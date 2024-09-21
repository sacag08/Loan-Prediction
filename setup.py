from setuptools import find_packages,setup
from typing import List

def get_requirements(filepath:str)->List[str]:
    requirements = []
    with open(filepath) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    print(requirements)
    return requirements

setup(
    name = "Online Shopping Intention",
    version = "0.0.1",
    author = "Sachit",
    author_email = "sachitagarwal98@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)
