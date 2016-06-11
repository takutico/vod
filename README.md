# Django Simple Video On Demand
Simple Media App VOD (Video On-Demand) application that keeps track of a list of videos the user has watched.

## Demo Site
http://vod.yamaguchipadilla.com/
If you want to get movies data as a JSON http://vod.yamaguchipadilla.com/api/movies/?format=json

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

You can check it in http://127.0.0.1:8000/

If you want to get just the movies data as a JSON http://127.0.0.1:8000/api/movies/?format=json

## Documents

You can find more documents [Here](docs/) about installation in [AWS](docs/aws.md), other [options](docs/options.md) like integration with MySQL, my [technical recommendation](docs/Technologies_to_use.md) if you are going to launch it tc...