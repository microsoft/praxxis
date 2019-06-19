import setuptools
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
     name='mtool', 
     python_requires = '>3.7', 
     version='0.0.0',
     author="Skyler Clark",
     author_email="example@microsoft.com",
     description="mtool",
     long_description=long_description,
     entry_points = {
     'console_scripts': ['m=src.mtool.app:start'],
     },
   long_description_content_type="text/markdown",
     url="mtool.github.com",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
     ],
 )