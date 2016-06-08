import json
import logging
import traceback
import urllib

from django.shortcuts import render

from movies.models import Movie

logger = logging.getLogger(__name__)


def index(request):
    data_list = movie_list = None
    try:
        # loading data from url
        url = "https://demo2697834.mockable.io/movies"
        response = urllib.request.urlopen(url)
        data_list = json.loads(response.read().decode('utf-8'))
        # print(data_list)

        for k in data_list['entries']:
            print(k)

        movie_list = Movie.objects.all()

        # If we want to load data from file, we can use next code
        # with open('publics/data.json', encoding='utf-8') as data_file:
        #     data = json.loads(data_file.read())
        # print(data)
    except:
        logger.error(traceback.format_exc())

    context = {
        'data_list': data_list['entries'],
        'movie_list': movie_list
    }
    return render(request, 'publics/index.html', context)
