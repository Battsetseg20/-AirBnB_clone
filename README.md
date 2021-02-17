<p align="center">
  <img width="409" height="128" src="https://www.holbertonschool.com/holberton-logo.png">
</p>

# AirBnB_clone

The AirBnB Console project is the first step towards the implementation of a simple copy of the AirBnB website. Here we will create our data model, manage the object via command interpreter, store and persis objects to a file. (JSON file)

### Files and Directories
- **models** directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- **tests** directory will contain all unit tests.
- **console.py** file is the entry point of our command interpreter.
- **models/base_model.py** file is the base class of all our models. It contains common elements:
- **models/engine** directory will contain all storage classes (using the same prototype). For the moment we will have only one: **file_storage.py**.


### Console
** What's the console and how to use it?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

Run ./console.py to start it in interactive mode.

```
$ ./console.py
(hbnb)
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)quit
$
```
## Example
**Start the console**
```
$ ./console.py
(hbnb)
```

**Creating a new instance**
```
(hbnb) create
** class name missing **
(hbnb) create BaseModel
f107c026-28e6-4f79-80fd-12e1d58221ca
```
**Show the instance**
```
(hbnb) show
** class name missing **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel f107c026-28e6-4f79-80fd-12e1d58221ca
[BaseModel] (f107c026-28e6-4f79-80fd-12e1d58221ca) {'id': 'f107c026-28e6-4f79-80fd-12e1d58221ca', 'created_at': datetime.datetime(2021, 2, 17, 19, 40, 29, 391412), 'updated_at': datetime.datetime(2021, 2, 17, 19, 40, 29, 391412)}
```
**Delete the instnace**
```
(hbnb) destroy BaseModel f107c026-28e6-4f79-80fd-12e1d58221ca
(hbnb) show BaseModel f107c026-28e6-4f79-80fd-12e1d58221ca
** no instance found **
```

