# 0x00. AirBnB clone - The Console
## The Holberton B&B

### About
Write command interpreter to manage AirBnb objects
* put in place parent class (`BaseModel`) to take care of initialization, serialization, and deserialization of future instances
* create simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnb (`User, State, City, Place…`) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage
* create all unittests to validate all our classes and storage engine


## Usage
Like the Unix shell, the HBnB console works in both interactive and non-interactive modes. In interactive mode, it prints a prompt and waits for input from the user.


#### Interactive Mode
To begin interactive mode, run ```./console.py``` from the command line

COMMAMND | DESCRIPTION
----|----
```(hbnb) quit``` | Quits console
```(hbnb) EOF``` | Quits console via EOF
```(hbnb) help <command>``` | Display help for <command>
```(hbnb) create <class>``` | Create object and print id
```(hbnb) show <class> <id>``` | Show information about an object
```(hbnb) destroy <class> <id>``` | Destroy object
```(hbnb) all <class>``` | Show all instances of a class
```(hbnb) update <class> <id> <attribute name> <attribute value>``` | Creates or updates the attribute of a class


The commands create, show, destroy, all, and update can also be ran with the following syntax:
```<class>.<command>(<optional id>, <optional arguments>)```

Running the update() function to create a new instance of 'middle_name' for the User class this way would look like this:
```update.User("123-123-123-123", middle_name, Davmas)```

#### Non-interactive Mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
```


## Running the Tests
All tests are located in the [tests](./tests/) folder.

To run unittests for this program, cd into root directory and run the following command:
`python3 -m unittest discover tests`

Tests can be modified in the tests/ directory


## Files Used in this Project
Models for all classes are located in the [models](./models/) folder.

FILE | DESCRIPTION | ATTRIBUTES
----|----|----
[file_storage.py](./models/engine/file_storage.py) | Storage for saving information | __file_path, __objects
[base_model.py](./models/base_model.py) | BaseModel class for all classes | id, created_at, updated_at
[user.py](./models/user.py) | User class | first_name, last_name, email, password
[amenity.py](./models/amenity.py) | Amenity class | name
[city.py](./models/city.py) | City class | state_id, name
[state.py](./models/state.py) | State class | name
[place.py](./models/place.py) | Place class | amenity_id, city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude
[review.py](./models/review.py) | Review class | place_id, user_id, text


## Built With
* [Python 3.4.3](https://www.python.org/download/releases/3.0/) - Python3 Language
* [PEP8 1.7](https://www.python.org/dev/peps/pep-0008/) - PEP8 style guide
* [Ubuntu 14.04 LTS](http://releases.ubuntu.com/14.04/) - Compiled on


### Authors
David Kwan - [github.com/dwkwan](https://github.com/dwkwan) <br>
Thomas Graeff - [github.com/graefft](https://github.com/graefft)
