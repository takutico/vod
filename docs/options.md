# Using MySQL

You should install mysqlclient

Activate virtualenv

```$ source VENV_PATH/bin/activate```

You may need to install the Python and MySQL development headers and librariessudo

```sudo apt-get install python3-dev libmysqlclient-dev```

Install python MySQL client

```pip install mysqlclient```

You need to edit setting file, you can find more info [here](https://docs.djangoproject.com/en/1.9/ref/databases/#connecting-to-the-database)


# Import from API

You can import [this](https://demo2697834.mockable.io/movies) API to this system using python shell

Activate virtualenv

```$ source VENV_PATH/bin/activate```

Use python shell to use project functions

```$ python manage.py shell```

If you want to use a specific setting file

```$ python manage.py shell --settings=SETTING_FILE```


Now we are in python shell

First need to import specific files

```
>>> from publics import views
>>> views.import_data()
```

