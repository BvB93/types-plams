import sys
from setuptools import setup

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
        'scm.plams',
        'scm.plams.molecule'
    ],
    package_dir={'scm-stubs.plams': '.'},
    package_data={'scm-stubs': ['py.typed', '*.pyi']},
)
