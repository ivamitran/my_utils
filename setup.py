from setuptools import setup, find_packages

setup(
    name="my_utils",  # name of library
    version="0.1.0",  # library version
    description="A utility library for my personal use",
    author="ivamitran",
    url="https://github.com/ivamitran/my_utils",  # URL of the project
    packages=find_packages(),  # Automatically finds and includes all packages
    # no dependencies
)