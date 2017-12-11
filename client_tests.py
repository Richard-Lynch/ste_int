#!/Users/richie/miniconda3/bin/python3

import requests

address = 'http://127.0.0.1:8050/files/'


def print_response(f):
    def wrapped_f(*args, **kwargs):
        r = f(*args, **kwargs)
        print(r)
        print(r.json())

    return wrapped_f


@print_response
def get_file_with_path(_id):
    return requests.get(address + "0", json={'message': msg})


@print_response
def get_file_with_id(_id):
    return requests.get(address + str(_id))


@print_response
def add_file(name, content):
    return requests.post(
        address + "0",
        json={
            'message': {
                'name': name,
                'content': content,
            },
        })


@print_response
def edit_file(_id, name, content):
    msg = {'name': name, 'content': content}
    msg = {k: v for k, v in msg.items()}
    return requests.put(address + "0", json={'message': msg})


@print_response
def del_file(_id):
    return requests.delete(address + str(_id))


add_file('test_file_name.txt', 'HELO WORLD')
get_file_with_path(1)
get_file_with_id(1)
edit_file(1, None, 'GOODBYE WORLD')
del_file(1)
