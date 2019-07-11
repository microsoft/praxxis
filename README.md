```
               ██ |                        ██ |  
██████\████\ ██████\    ██████\   ██████\  ██ |  
██  _██  _██\\_██  _|  ██  __██\ ██  __██\ ██ |  
██ / ██ / ██ | ██ |    ██ /  ██ |██ /  ██ |██ |  
██ | ██ | ██ | ██ |██\ ██ |  ██ |██ |  ██ |██ |  
██ | ██ | ██ | \████  |\██████  |\██████  |██ |  
\__| \__| \__|  \____/  \______/  \______/ \__|
```

## Introduction
mtool is a task interface built on big data and machine learning. Using your own local storage pool to collect data on your habits when running notebooks, mtool will learn about the problems you are solving, correlate that with the problems everyone else is solving, and predict the next notebook you should run without interrupting your workflow. It is a tool based on a collaborative paradigm of problem solving, allowing every person to leverage everyone's knowledge to come to a solution more quickly.

Using mtool, any command can be run, documented, and reproduced using executable code cells in jupyter notebooks. By using notebooks to execute, mtool enforces that your your workflows are well documented and replicable, allowing even the least technical user to jump in right where you left off. In exchange, even the most frustrating sequence of commands can be processed by simply typing "m 1".

## Installation 
git clone this repo, and run 
``` 
python setup.py install
pip install -r requirements.txt
```
mtool requires python 3.6 and above.

## Features
##### Scenes
mtool scenes are situation-specific configurations that can be saved, closed, reopened and shared. Scenes store your habits, history environment, allowing you to easily fix old problems, and get help with new ones. When you share your scenes, your peers are able to see the same outputs, predictions, history, and parameter values you see, effectively containerizing a working environment.

##### Predictions 
With or without a big data cluster, mtool's predictions are usable through trained machine learning models distributed by Microsoft. If you have your own big data cluster, you can top up or train a new model with your own data.

##### History
With mtool, a history of commands is preserved, allowing you to backtrack through problems and move forward quickly through complex problems. Since situation specific configurations are saved as environment variables in scenes, you'll always be able to track exactly what commands were run, what was changed, and where you need to go next.

##### Notebook Libraries
mtool runs on libraries of notebooks, allowing every command on your system to be documented and explained in a beautiful markdown format. mtool combines the idea of functional documentation with every part of a system, allowing every person on a team to operate with the same understanding as even the most senior engineer, through guarunteed useful docs.

##### Environments
mtool uses parameterized jupyter notebooks to inject environments into code cells. By saving environments through mtool, envionments are saved through sessions and restarts, and are documented in an easily accessible format, allowing you to run every notebook with absolute certainty. 

## Extra mtool 
For more infromation on how to use m tool type m --help into the command 
