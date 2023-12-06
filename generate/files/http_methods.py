import requests

def get_http_method(url: str):
    response = requests.get(url)
    return response

def post_http_method(url: str):
    response = requests.post(url)
    return response

def put_http_method(url: str):
    response = requests.put(url)
    return response

def patch_http_method(url: str):
    response = requests.patch(url)
    return response

def delete_http_method(url: str):
    response = requests.delete(url)
    return response

