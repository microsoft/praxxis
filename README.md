[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
<img alt="praxxis logo" src="https://raw.githubusercontent.com/microsoft/praxxis/master/docs/images/praxxis_logo_black.png">
</div>

  <p align="center">
    A Command Line Notebook Task Interface
    <br />
    <a href="https://github.com/microsoft/praxxis/tree/master/docs"><strong>Explore the docs </strong></a>
    <br />
    <br />
    <a href="https://github.com/microsoft/praxxis/issues">Report Bug</a>
    .
    <a href="https://github.com/microsoft/praxxis/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Features](#features)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

praxxis is a task interface built on big data and machine learning. Using your own storage pool to collect data on your notebook-running habits, praxxis will learn about the problems you are solving, correlate that with the problems everyone else is solving, and predict the next notebook you should run without interrupting your workflow. It is a tool based on a collaborative paradigm of problem solving, allowing every person to leverage the knowledge of their larger organization to come to a solution more quickly.

Using praxxis, any command can be run, documented, and reproduced using executable code cells in jupyter notebooks. By using notebooks to execute, praxxis enforces that your workflows are well documented and replicable, allowing even the least technical user to jump in right where you left off. In exchange, even the most frustrating sequence of commands can be processed by simply typing "prax 1".

### Features
#### Scenes
praxxis scenes are situation-specific configurations that can be saved, closed, reopened and shared. Scenes store your execution history and parameter settings, allowing you to easily fix old problems and get help with new ones. When you share your scenes, your peers are able to see the same outputs, predictions, history, and parameter values you see, effectively containerizing a working environment.

#### Predictions 
With or without a big data cluster, praxxis's predictions are usable through trained machine learning models. If you have your own big data cluster, you can top up or train a new model with your own data. With some configuration, the training code can be run locally as well.

#### History
With praxxis, a history of commands is preserved, allowing you to backtrack through problems and move forward quickly through complex problems. Since situation specific configurations are saved as parameters in scenes, you'll always be able to track exactly what commands were run, what was changed, and where you need to go next.

#### Notebook Libraries
praxxis runs on libraries of notebooks, allowing every command on your system to be documented and explained in a beautiful markdown format. praxxis combines the idea of functional documentation with every part of a system, allowing every person on a team to operate with the same understanding as even the most senior engineer, through docs that remain up to date because they're packaged with executable solutions.

#### Parameters
praxxis uses parameterized jupyter notebooks to inject parameters into code cells. By saving parameters through praxxis, parameters are saved through sessions and restarts, and are documented in an easily accessible format, allowing you to run every notebook with absolute certainty. 



<!-- GETTING STARTED -->
## Getting Started

to get started developing or using praxxis, follow these steps.

### Prerequisites

- python 3.6 or above

### Installation
to install, simply run
```
pip install praxxis
```
or, for development mode clone the repo and run
```
pip install -e .
```



<!-- USAGE EXAMPLES -->
## Usage

praxxis is a command line tool for running jupyter notebooks. 
To run for the first time, open up your terminal after installing, and run 
```
prax
```
to see the help page. 

_For more examples, please refer to the [Documentation](https://github.com/microsoft/praxxis/blob/master/docs)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/microsoft/praxxis/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

We would love your help!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Praxxis uses pytest for testing, and it would be much appreciated if you could write tests for your changes before opening a pull request! 

We also reference [Python PEP-8](https://www.python.org/dev/peps/pep-0008/) for our coding style.

Please see our [contributing.md](https://github.com/microsoft/praxxis/blob/master/CONTRIBUTING.md) for more details on our coding standards, and code of conduct.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


Project Link: [https://github.com/microsoft/praxxis](https://github.com/microsoft/praxxis)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/microsoft/praxxis.svg?style=flat-square
[contributors-url]: https://github.com/microsoft/praxxis/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/microsoft/praxxis.svg?style=flat-square
[forks-url]: https://github.com/microsoft/praxxis/network/members
[stars-shield]: https://img.shields.io/github/stars/microsoft/praxxis.svg?style=flat-square
[stars-url]: https://github.com/microsoft/praxxis/stargazers
[issues-shield]: https://img.shields.io/github/issues/microsoft/praxxis.svg?style=flat-square
[issues-url]: https://github.com/microsoft/praxxis/issues
[good-first-issues-shield]: https://img.shields.io/github/issues/microsoft/praxxis.svg?style=flat-square
[issues-url]: https://github.com/microsoft/praxxis/issues
[license-shield]: https://img.shields.io/github/license/microsoft/praxxis.svg?style=flat-square
[license-url]: https://github.com/microsoft/praxxis/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png

<!-- readme template from https://github.com/microsoft/praxxis-->