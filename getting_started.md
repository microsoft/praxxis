#Praxxis
## getting started

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

to run a notebook, run
```
prax l
```
to see what notebooks are available, and
```
prax <ordinal or name>
```
to run based on the name or ordinal in the list.

To open a notebook, praxxis offers a few options.
```
prax o <name or ordinal> html
prax o <name or ordinal> jupyter
prax o <name or ordinal> ads
```
opens notebooks in html, jupyter or Azure Data Studio, respectively.
To open the notebook in vim, use the default command
```
prax o <name or ordinal>
```

## Setting Up Telemetry

By default, praxxis stores no information on your notebook habits, but in order to use predictions, you need to link your install to some type of external storage, so that a machine learning model can be trained.

In order to access the telemetry setup utility, run

```
prax u
```
and use ordinals to select settings.

#####Telemetry
to turn telemetry on and off, select telemetry from the list, and set the value to 1 for on, and 0 for off.
#####URL
this is the url of the storage pool. The default url is set to a SQL server instance, but  it can be changed to anything.
#####Host
this is the IP of the host machine that you want to send data to.
#####Username
this is the username of the login that you want to use to send data.
#####Password
this is the password of the login that you want to use to send data.

If you've set up all of these things correctly, then you should be able to use praxxis, and see data on notebook execution appearing in your cluster.
