import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
     name='mtool',  
     version='0.0.0',
     scripts=['scripts/m.cmd', 'scripts/mtool/installer.cmd'] ,
     author="Skyler Clark",
     author_email="example@microsoft.com",
     description="mtool",
     long_description=long_description,
     
   long_description_content_type="text/markdown",
     url="mtool.github.com",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
     ],
 )