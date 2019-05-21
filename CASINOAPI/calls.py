import requests


def get_data():
    response = requests.get('http://httpbin.org/get')
    #import pdb; pdb.set_trace()

    return response.status_code