# Django Simple Video On Demand
Simple Media App VOD (Video On-Demand) application that keeps track of a list of videos the user has watched.

## Demo Site
http://vod.yamaguchipadilla.com/

This site is located in AWS

## Run Application in Local
Create a project directory and go inside
```
mkdir vod
cd vod
```
Clone VOD project from github

```git clone https://github.com/takutico/vod.git```

Create a virtualenv (for more information about virtualenv go [here](https://virtualenv.pypa.io/en/stable/installation/))

```virtualenv -p python3 venv```

Activate virtualenv

```source venv/bin/activate```

Install all requirements

```pip install -r vod/requirements.txt```

Run server

```python vod/manage.py runserver```

You can check it http://127.0.0.1:8000/

## Documents

You can find more documents [Here](docs/) about installation in AWS, integrate with MySQL, etc...