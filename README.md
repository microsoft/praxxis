[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Good First Issues][good-first-issue-shield]][good-first-issue-url]
[![MIT License][license-shield]][license-url]
[![Chatting][chat-shield]][chat-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
<img alt="praxxis logo" src="https://raw.githubusercontent.com/microsoft/praxxis/master/docs/images/praxxis_logo_black.png">
</div>

  <p align="center">
    A Command Line Notebook Task Interface
    <br />
    <a href="https://microsoft.github.io/praxxis/"><strong>Explore the docs </strong></a>
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

praxxis is a task interface built on big data and machine learning. Using your own storage pool to collect data on your habits when running notebooks, praxxis will learn about the problems you are solving, correlate that with the problems everyone else is solving, and predict the next notebook you should run without interrupting your workflow. It is a tool based on a collaborative paradigm of problem solving, allowing every person to leverage everyone's knowledge to come to a solution more quickly.

Using praxxis, any command can be run, documented, and reproduced using executable code cells in jupyter notebooks, allowing even the least technical user to jump in right where you left off.

### Features
#### Scenes
praxxis scenes are situation-specific configurations that can be saved, closed, reopened and shared. Scenes store your habits, history, and parameter settings, allowing you to easily fix old problems and get help with new ones. When you share your scenes, your peers are able to see the same outputs, history, and parameter values you see, allowing for easier problem solving in groups.

#### Predictions 
With or without a storage pool, praxxis's predictions are usable through trained machine learning models. If you have your own storage pool, you can top up or train a new model with your own data.

#### History
Using praxxis, a history of commands is preserved, allowing you to backtrack through problems. Since situation specific configurations are saved as parameters in scenes, you'll always be able to know exactly what commands were run, what was changed, and where you need to go next.

#### Notebook Libraries
Praxxis runs on libraries of jupyter notebooks, allowing every command on your system to be documented and explained in a useful markdown format. By directly running the code embedded in the documentation, you know that no information is being lost, and no documentaion is getting out of date.

#### Parameters
Praxxis uses parameter tags to inject parameters into code cells. By saving parameters through praxxis, your environments are saved through sessions and restarts, and are documented in an easily accessible format.



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

_For more examples, please refer to the [Documentation](https://microsoft.github.io/praxxis/)_



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

[good-first-issue-shield]: https://img.shields.io/github/issues/microsoft/praxxis/good%20first%20issue?style=flat-square
[good-first-issue-url]: https://github.com/microsoft/praxxis/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22

[license-shield]: https://img.shields.io/github/license/microsoft/praxxis.svg?style=flat-square
[license-url]: https://github.com/microsoft/praxxis/blob/master/LICENSE.txt

[chat-shield]: https://img.shields.io/matrix/praxxis:matrix.org?style=flat-square
[chat-url]: https://riot.im/app/#/room/#praxxis:matrix.org

<!-- readme template from https://github.com/microsoft/praxxis-->