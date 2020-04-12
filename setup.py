import os
import sys
from typing import List, Dict
from setuptools import setup


def find_stubs(package: str) -> Dict[str, List[str]]:
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, '', 1)
            stubs.append(path)
    return {package: stubs}


install_requires = ['numpy', 'plams']
if sys.version_info < (3, 8):
    install_requires.append('typing_extensions')

setup(
    name='plams-stubs',
    version='1.4',
    license='LGPLv3',
    python_requires='>=3.6',
    install_requires=install_requires,
    packages=[
        'scm-stubs'
    ],
    package_data=find_stubs('scm-stubs')
)
