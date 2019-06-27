# Item Catalog

Item Catalog is the second project for Udacity's Full Stack Web Developer Nanodegree Program.

## Project Overview

Item Catalog provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## Instructions

1 Download and install [Python](https://www.python.org/)
2 Download and install [virtual box](https://www.virtualbox.org/)
3 Download and install [vagrant](https://www.vagrantup.com/)
4 Clone this repository
5 Place the Item Catalog folder in your Vagrant directory
6 Launch Vagrant

```
$ vagrnt up
```

7 Login to vagrant

```
$ vagrant ssh
```

8 Change directory to ```/vagrant```

```
$ cd /vagrant
```

9 Run ```database_setup.py``` file to initialize *Database*

```
$ python database_setup.py
```

10 Run ```menus.py``` to populate database with some initial data

```
$ python menus.py
```

11 Run ```project.py``` file to launch the project

```
$ python project.py
```

12 Open browser and visit [http://localhost:5000](http://localhost:5000)

## API JSON Endpoints

These JSON endpoints will return the information in JSON format

### To get all available restaurants

```
/restaurants/JSON
```

### To get all available menus of a specific restaurant

```
/restaurants/<int:restaurant_id>/menu/JSON
```

### To get information about a specific menu item

```
/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON
```
