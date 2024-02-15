from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
import requests
import time
def data_factory(url):
    data = requests.get(url)
    return data.json()


def filter_data(data, requred_data):
    if isinstance(data, list):
        for i in data:
            extra_keys = i.keys() - requred_data
            if extra_keys:
                for j in extra_keys:
                    i.pop(j)
    else:
        extra_keys = data.keys() - requred_data
        for i in extra_keys:
            data.pop(i)
    return data


def index(request):
    _data = filter_data(data_factory(url="https://jsonplaceholder.typicode.com/posts"), {"title", "body"})
    return JsonResponse(_data, safe=False)

def get_products(request):
    _data = filter_data(data_factory(url="https://fakestoreapi.com/products"), {"title", "price", "description", "rating"})
    return JsonResponse(_data, safe=False)


def generate_content():
        for i in range(10):
            yield f"Chunk {i}\n"
            time.sleep(1)

import csv

def generate_large_csv():
    # Example data to be written into the CSV file
    data = [
        ['Name', 'Age', 'Country'],
        ['John Doe', 30, 'USA'],
        ['Jane Smith', 25, 'Canada'],
        # Add more data here...
    ]

    for row in data:
        yield ','.join(map(str, row)) + '\n'

def streaming(request):
    return StreamingHttpResponse(streaming_content=generate_large_csv())
