<p align="center">
  <img width="409" height="128" src="https://www.holbertonschool.com/holberton-logo.png">
</p>

<h1 align="center">AirBnB clone project</h1>

## AirBnB Console

The AirBnB Console project is the first step towards the implementation of a simple copy of the AirBnB website. Here we will create our data model, manage the object via command interpreter, store and persis objects to a file. (JSON file)

### Files and Directories
- **models** directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- **tests** directory will contain all unit tests.
- **console.py** file is the entry point of our command interpreter.
- **models/base_model.py** file is the base class of all our models.
- **models/engine** directory will contain all storage classes (using the same prototype). For the moment we will have only one: **file_storage.py**.


### Console
**What's the console and how to use it?**
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
Or, use echo to run it in non-interactive mode.
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

### Supported commands

| Command  | Syntax                        |Description                                    |  
|:-------: | ------------------------------|----------------|  
| `help`   |`help`                         |to get help about other commands.             |  
| `quit`   |`quit`                         |or `EOF` (end of file) to terminate session.   | 
| `create` |`create <class>`               |creates an object |
|`show`    |`show <class name> <id>`       |prints the string representation of an object|
| `destroy`|`destroy <class> <id>`         |deletes an object|
|`all`     |`all <class>` OR `all`         |shows all representations of objects|
|`update`  |`update <class> <id> <attribute> "<value>"`	      |updates attributes of object|


## Example
**Start the console**
```
$ ./console.py
(hbnb)
```

**To create new instance**
```
(hbnb) create
** class name missing **
(hbnb) create BaseModel
f107c026-28e6-4f79-80fd-12e1d58221ca
```
**To show the instance**
```
(hbnb) show
** class name missing **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel f107c026-28e6-4f79-80fd-12e1d58221ca
[BaseModel] (f107c026-28e6-4f79-80fd-12e1d58221ca) {'id': 'f107c026-28e6-4f79-80fd-12e1d58221ca', 'created_at': datetime.datetime(2021, 2, 17, 19, 40, 29, 391412), 'updated_at': datetime.datetime(2021, 2, 17, 19, 40, 29, 391412)}
```
**To delete the instance**
```
(hbnb) destroy BaseModel f107c026-28e6-4f79-80fd-12e1d58221ca
(hbnb) show BaseModel f107c026-28e6-4f79-80fd-12e1d58221ca
** no instance found **
```

## AirBnB - Web Static
Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

- Create simple HTML static pages
- Style guide
- Fake contents
- No Javascript
- No data loaded from anything
During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

### Example
<p align="center">
  <img width="902" height="614" src="https://github.com/Battsetseg20/AirBnB_clone/blob/main/web_static/images/Output.png">
</p>



**Holberton School**
Battsetseg Yondongombo Cohort 13
