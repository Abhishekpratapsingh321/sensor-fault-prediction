from setuptools import find_packages,setup
from typing import List

require_file_name="requirements.txt"
Hypen_e_dot="-e ."

def get_requirements()->List[str]:
    with open(require_file_name) as file_require:
        requirement_list=file_require.readlines()
    requirement_list=[requirement_name.replace("\n","") for requirement_name in requirement_list]
    if Hypen_e_dot in requirement_list:
        requirement_list.remove(Hypen_e_dot)
    return requirement_list


setup(
    name="sensor",
    version="0.0.1",
    author="pratap",
    author_email="pratapsinghabhishek112@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)