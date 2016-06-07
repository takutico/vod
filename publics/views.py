import json
import urllib

from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):

    # loading data from url
    url = "https://demo2697834.mockable.io/movies"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode('utf-8'))
    print(data)

    # If we want to load data from file, we can use next code
    # with open('publics/data.json', encoding='utf-8') as data_file:
    #     data = json.loads(data_file.read())
    # print(data)

    return render(request, 'publics/index.html', {})
    # return HttpResponse("Hello, world. You're at the polls index.")
