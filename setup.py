from setuptools import setup

setup(
    name="plams-stubs",
    version="1.5.1",
    license="LGPLv3",
    python_requires=">=3.6",
    install_requires=["numpy>=1.21", "pandas-stubs"],
    packages=["scm-stubs"],
    package_data={"scm-stubs": ["py.typed", "**/*.pyi"]},
)
