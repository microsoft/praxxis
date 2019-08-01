# Executable Documentation in the Command Line with Praxxis

By Amanda Bertsch and Skyler Clark 

Jupyter notebooks are a powerful tool, popular among data scientists for data visualization, interactive output, and code sharing. Interest in using Jupyter notebooks has grown over the last several years to include corporate applications, such as [Netflix's use of notebooks](https://medium.com/netflix-techblog/notebook-innovation-591ee3221233) to manage large data workloads at scale. 

A major benefit of notebooks is the packaging of documentation (in the form of markdown 'cells,' or document sections) in the same document as executable code, making it simple to update documentation at the same time as the related code. Here at Microsoft, the Azure Data team is actively pushing for the use of notebooks as an executable form of documentation, combining the immediate usefulness of a script with the informative value of a how-to guide. 

One of the most valuable use cases for executable documentation is troubleshooting. Sharing a notebook as a troubleshooting solution allows users to offer both immediate, practical resolution to a problem and the associated explanation of the solution in one readable format. 

However, notebooks are not perfect. Editing notebooks to be applicable to a particular troubleshooting scenario can involve adding sensitive information that cannot be shared, and the output of past executions is erased as soon as the notebook is re-run. Choosing the correct sequence of notebooks to run can be difficult, and editing variables across a set of notebooks is time-consuming and error-prone. 

Praxxis offers a solution to these pain points. Praxxis is a command-line tool for parameterizing and executing sequences of notebooks, as well as predicting the next notebook to run in a workflow. Leveraging a server storage pool, praxxis saves the output of every notebook execution across an organization and trains a model to predict sequences to execute, removing the effort from sharing workflows and empowering an entire organization to learn from each other over time.

Praxxis offers features for the entire notebook experience, including loading sets of notebooks to use, injecting parameters, sharing and saving working environments, creating pathways through execution based on notebook output, 


### Git integration

Adding notebooks to your workflow has never been easier, with built-in support for pulling a set of notebooks from a git remote.


### Parameter Injection
Praxxis wraps the parameter injection capabilities of [papermill](https://github.com/nteract/papermill), a tool that allows for runtime parameterization of notebooks executed on the command line. Papermill requires each notebook execution to pass the parameters to inject as part of a command; thus, executing a notebook requires opening the notebook to view parameter names, copying those names, typing them, and typing the values to override with. This process requires the user to leave the command line to view parameters and introduces a potential for typing errors that multiplies for every notebook run.

Praxxis introduces the concept of a scene as a solution to this problem. Parameters are defined for one workflow, with values set once and then injected into every notebook that has those parameters. That means that a value can be set once and then used for all notebooks in a library, saving time and eliminating the potential for errors as a value is retyped over and over. 

Praxxis also allows users to pull a set of parameters from a single notebook or an entire library into a scene, so the default values can be viewed and overridden without every opening a notebook. 


### Rulesets

### Machine Learning
--pulling libraries from git

--rulesets 

--machine learning



[ktool](https://twitter.com/melaniecebula/status/1073415598934155264?lang=en)