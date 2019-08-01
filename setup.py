import setuptools
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
     name='praxxis', 
     python_requires =  '>=3.6.*',
     install_requires=[
        "urllib3",
        "requests",
        "papermill",
        "ijson",
        "ipykernel", 
        "setuptools",
        "nbopen",
        "gitpython",
        "toml",
        "giturlparse",
        "colorama",
        "toml"
     ],
     version='0.1.0',
     author="Skyler Clark, Amanda Bertsch, Swarathmika Kakivaya, Stuart Padley",
     author_email="skylerjaneclark@gmail.com, abertsch72@gmail.com, swarathmika@hotmail.com",
     description="a notebook task interface built on big data and machine learning.",
     long_description=long_description,
     license = "MIT",
     entry_points = {
     'console_scripts': ['prax=src.praxxis.app:start'],
     },
   long_description_content_type="text/markdown",
     url="https://github.com/microsoft/praxxis",
     packages=setuptools.find_packages(),
     classifiers=[
        'Programming Language :: Python :: 3.7',
      ],
 )