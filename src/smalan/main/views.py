
from django.shortcuts import render_to_response

from smalan.util import add_response


@add_response
def main(request, response):
    render_to_response('main.html')


@add_response
def test(request, response):
    response['asdf'] = 3
    render_to_response('test.html')
