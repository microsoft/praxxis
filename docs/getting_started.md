#Praxxis
## Getting Started

To get started with praxxis, you need
 - python 3.6 installed
 - the repo cloned


To install in production mode, move to the root of the repo and run

```
pip install .
```
in the command line.

This will install praxxis onto your machine, and allow you to run commands with
```
prax
```

On your first run, praxxis will set up the directories and databases it needs to store data and run.

### Importing Libraries
praxxis can import libraries from anywhere on your machine, or through a hosted git service. As of right now, the project supports GitHub, GitLab, and BitBucket for remote repositories.

To get started with test notebooks, run
```
prax al tests/test_notebooks
```

This will load the pre-written test notebooks into your session.

To check that the library has been loaded properly, run
```
prax ll
```
And verify that the library "test_notebooks" is loaded.

To check that the notebooks have been loaded properly, run
```
prax l
```

You should be able to see the notebooks "broken_notebook, test_notebook, test_param_inject".

You can also import a library of notebooks from a git remote by using the same al command.
```
prax al <your git url>
```

###Using Notebooks
Now that you have your notebooks loaded into praxxis, you can use them!

First view what notebooks you have loaded by running
```
prax l
```
This should display the notebooks, and in what libraries they are located.

#### Running notebooks

In order to run a notebook, run
```
prax <ordinal or name>
```
praxxis also supports running a notebook with the html flag, which allows you to open the output file in a browser.
```
prax <ordinal or name> html
```

#### Opening notebooks

To open a notebook, praxxis offers a few options.
```
prax o <name or ordinal> html
prax o <name or ordinal> jupyter
prax o <name or ordinal> ads
```
opens notebooks in HTML, Jupyter or Azure Data Studio, respectively.
To open the notebook in vim, use the default command
```
prax o <name or ordinal>
```
#### Using Parameters
Some notebooks have parameters that can be injected, allowing the notebook's functionality to be changed without editing the notebook itself. Praxxis supports parameter injection into any notebook with the first code cell tagged as a parameter cell.


##### Notebook Parameters
To view the parameters that can be set in a certain notebook, run
```
prax v <notebook name or ordinal>
```
to pull those parameters out of a notebook and into your scene, run
```
prax p <notebook name or ordinal>
```

##### Library Parameters
to view the parameters that can be set throughout a library, run
```
prax vl <library name or ordinal>
```
to pull those parameters out of the library and into your scene, run
```
prax pl <library name or ordinal>
```
##### Parameter Operations
Existing parameters can be set or updated by running
```
prax sp <name or ordinal> <value>
```
and deleted by running
```
prax dp <name or ordinal>
```
and viewed by running
```
prax lp
```
To try out injecting a parameter yourself, run these commands in the root of your praxxis folder.
```
prax al tests/test_notebooks
prax l
prax v test_param_inject
prax p test_param_inject
prax se 1 "hello test!"
prax r test_param_inject
```

You should be able to see the notebooks you've imported, test_param_inject's parameters, pulled those parameters into your working scene, set them, and seen the output of the notebook with the new injected parameters.


## Setting Up Telemetry

By default, praxxis stores no information on your notebook habits, but in order to use predictions, you need to link your install to some type of external storage. This allows for a machine learning model to be built on your habits.

In order to access the telemetry setup utility, run

```
prax u
```
and use ordinals to select settings.

####Telemetry
to turn telemetry on and off, select telemetry from the list. Set the value to 1 for on, and 0 for off.
####URL
this is the url of the storage pool. The default url is set to a SQL server instance, but it can be changed to anything.
####Host
this is the IP of the host machine that you want to send data to.
#####Username
this is the username of the login that you want to use to send data.
####Password
this is the password of the login that you want to use to send data.

If you've set up all of these things correctly, then you should be able to use praxxis and see data on notebook execution appearing in your cluster.
