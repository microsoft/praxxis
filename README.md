![praxxis logo](docs/images/praxxis.png)
## Introduction
praxxis is a task interface built on big data and machine learning. Using your own storage pool to collect data on your habits when running notebooks, praxxis will learn about the problems you are solving, correlate that with the problems everyone else is solving, and predict the next notebook you should run without interrupting your workflow. It is a tool based on a collaborative paradigm of problem solving, allowing every person to leverage everyone's knowledge to come to a solution more quickly.

Using praxxis, any command can be run, documented, and reproduced using executable code cells in jupyter notebooks, allowing even the least technical user to jump in right where you left off.

## Installation 
git clone this repo, and run 
``` 
pip install .
```
or 
``` 
pip install -e .
```
for development mode.

## Features
#### Scenes
praxxis scenes are situation-specific configurations that can be saved, closed, reopened and shared. Scenes store your habits, history, and parameter settings, allowing you to easily fix old problems and get help with new ones. When you share your scenes, your peers are able to see the same outputs, history, and parameter values you see, allowing for easier problem solving in groups. 

#### Predictions 
With or without a storage pool, praxxis's predictions are usable through trained machine learning models distributed by Microsoft. If you have your own storage pool, you can top up or train a new model with your own data.

#### History
With praxxis, a history of commands is preserved, allowing you to backtrack through problems. Since situation specific configurations are saved as parameters in scenes, you'll always be able to know exactly what commands were run, what was changed, and where you need to go next.

#### Notebook Libraries
praxxis runs on libraries of jupyter notebooks, allowing every command on your system to be documented and explained in a useful markdown format. By directly running the code embedded in the documentation, you know that no information is being lost, and no documentaion is getting out of date.

#### Parameters
praxxis uses parameterized jupyter notebooks to inject parameters into code cells. By saving parameters through praxxis, your environments are saved through sessions and restarts, and are documented in an easily accessible format.

## Usage
For more infromation on how to use praxxis tool type prax --help into the command, or check out the docs folder!
