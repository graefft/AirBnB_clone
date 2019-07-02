# 0x00. AirBnB clone - The Console

### About
Write command interpreter to manage AirBnb objects
* put in place parent class (`BaseModel`) to take care of initialization, serialization, and deserialization of future instances
* create simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnb (`User, State, City, Place…`) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage
* create all unittests to validate all our classes and storage engine

#### General
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage `datetime`
* What is an `UUID`
* What is `*args` and how to use it
* What is `**kwargs` and how to use it
* How to handle named arguments in a function

## Running the Tests
To run unittests for this program, cd into root directory and run the following command:
`python3 -m unittest discover tests`

Tests can be modified in the tests/ directory

## Built With
* [Python 3.4.3](https://www.python.org/download/releases/3.0/) - Python3 Language
* [PEP8 1.7](https://www.python.org/dev/peps/pep-0008/) - PEP8 style guide
* [Ubuntu 14.04 LTS](http://releases.ubuntu.com/14.04/) - Compiled on

### Authors
David Kwan - [github.com/dwkwan](https://github.com/dwkwan) <br>
Thomas Graeff - [github.com/graefft](https://github.com/graefft)
