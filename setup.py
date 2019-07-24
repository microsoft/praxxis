import setuptools
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
     name='praxxis', 
     python_requires = '>=3.7.*, >=3.6.*',
     install_requires=[
        "urllib3",
        "requests",
        "papermill",
        "ijson",
        "ipykernel", 
        "setuptools",
        "nbopen",
        "gitpython",
        "giturlparse",
        "colorama"
     ],
     version='0.1dev',
     author="Skyler Clark, Amanda Bertsch, Swarathmika Kakivaya, Stuart Padley",
     author_email="example@microsoft.com",
     description="praxxis",
     long_description=long_description,
     entry_points = {
     'console_scripts': ['prax=src.praxxis.app:start'],
     },
   long_description_content_type="text/markdown",
     url="github.com/microsoft/praxxis",
     packages=setuptools.find_packages(),
     classifiers=[
        'Programming Language :: Python :: 3.7',
      ],
 )