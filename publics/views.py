import json
import logging
import traceback
import urllib

from django.shortcuts import render

from movies.models import Movie

logger = logging.getLogger(__name__)


def index(request):
    movie_list = None
    try:
        movie_list = Movie.objects.all().order_by('?')[:10]
    except:
        logger.error(traceback.format_exc())

    context = {
        'movie_list': movie_list
    }
    return render(request, 'publics/index.html', context)


def import_data():
    # loading data from url
    # url = "https://demo2697834.mockable.io/movies"
    # response = urllib.request.urlopen(url)
    # data_list = json.loads(response.read().decode('utf-8'))
    # print(data_list)

    with open('publics/data.json', encoding='utf-8') as data_file:
        data_list = json.loads(data_file.read())
    # print(data)

    for data in data_list['entries']:
        try:
            Movie(
                description=data['description'],
                title=data['title'],
                id=data['id'],
                image=data['images'][0]['url'],
                url=data['contents'][0]['url'],
            ).save()
        except:
            print('Cannot create data')
            print(data)
            print(traceback.format_exc())
    return
