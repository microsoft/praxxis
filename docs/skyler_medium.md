If you've been in the data science world for any period of time, you probably have already heard of the jupyter notebook. An elegant, executable, markdown friendly document with specially marked cells for executing code in a number of "kernels" such as python or r. 

This technology has really been adopted by those in the data science field for a couple of reasons. 

- The format lends itself extremely well to sharing executed output with graphs, useful when you want to share your output for things like ML training graphs 
- Python is part of the backbone of jupyter, which is a language data scientists tend to prefer
- They're more interactive than an IDE, and better for prototyping
- It's easy to teach by example when the documentation and the code exist in the same place
- Documentation on the code and the code itself stay up to date by by being edited in the same place

But if you think about it, really anyone could benefit from any of these features. Having interactive, beautifully documented, shareable code that is easy to teach from could help anyone working on anything from troubleshooting to database management.

## _So why aren't we using them?_

A lot of the pain points of Jupyter come from the way that they have to be run. Since jupyter notebooks are a very visual format, running them out of a GUI can be challenging at times. 

Upon that, in order to set parameters, most of the time the notebooks must be edited directly to remove hardcoded defaults such as usernames and passwords. As a result, people need to edit every default in every notebook before it is run, save a copy, and hope it doesn't get shared, ultimately defeating the purpose of using a shareable format to begin with.

They're also sometimes hard to find! Even if you've written a huge library of useful notebooks for yourself and your friends, updating that library and searching through it without any kind of framework in place to help you could end up taking longer than just writing a new notebook.

There comes a time when the time it takes to find and run a notebook becomes more challenging than simply writing the code yourself. 


## Introducing Praxxis


With these issues in mind, we set out to be that change, and hopefully create tool to help the world move in the direction of executable documentation. 
Praxxis is a command line utility built with simplicity at its core.  With features like scenes, parameters, libraries, and predictions, we take the power of jupyter notebooks and make them accessible for everyone. 

### Praxxis Scenes
Scenes allow issue-specific workflows to be labeled, stored and shared. By saving parameters injected into the notebooks you run, notebooks can be run against entirely different environments, with different sets of parameters simply by using the command 
```
prax cs 
```
By keeping working environments labeled and independent, solutions can be returned to, ended, restarted and deleted with a few keyboard commands. 
Gone are the days of tedious parameter searching and re-writing of notebooks.

### Praxxis Parameters
Praxxis leverages the papermill API to inject parameters into notebooks at runtime. This allows users to set parameters for every notebook in a scene with the command 
```
prax sp
```
and run them without ever having to edit a single line of code. By doing this, notebooks can be shared without ever having to worry about leaking secrets or confusing people with your situation specific injects. 


### Praxxis Libraries 
Libraries of notebooks are organized by folder name, and can be pulled from a remote github repository or imported from any path on your machine.
By keeping organized with your notebooks, you know that you'll be able to quickly come back to something you've written.


### Praxxis Predictions 
Though the most powerful element of praxxis (and the reason for the name) is the ability to get predictions based on history from your entire organization. Using a storage pool, praxxis sends data on sequences of run notebooks, allowing a machine learning model to train on the habits of everyone providing data. 
Models can be updated, imported and deleted, allowing you to have full control on what kind of predictions you see for each situation.
If you don't have a model (or have an unhelpful one), sequences of notebooks can be defined using a rules engine, allowing people and your model to learn what steps they should take to come to a solution. 

## This is incredible! How do I get it!
Praxxis is currently installable with pip
```
pip install praxxis
```
The source is also available under the MIT license on github.com/microsoft/praxxis. The tool is currently in beta, but we're going to be gearing up for a full release as soon as we can!