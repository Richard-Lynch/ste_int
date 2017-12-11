#!/Users/richie/miniconda3/bin/python3

import requests

address = 'http://127.0.0.1:8050/files/'


def print_response(f):
    def wrapped_f(*args, **kwargs):
        r = f(*args, **kwargs)
        print(r)
        print(r.json())
        return r

    return wrapped_f


@print_response
def get_file_with_path(_id):
    msg = {'_id': _id}
    # msg = {k: v for k, v in msg.items()}
    return requests.get(address + "0", json={'message': msg})


@print_response
def get_file_with_id(_id):
    return requests.get(address + str(_id))


@print_response
def get_file_with_url(url):
    return requests.get(url)


@print_response
def add_file(name, content):
    return requests.post(
        address + "0",
        json={
            'message': {
                'name': name,
                'content': content,
                'your mom': 'glenna'
            },
        })


@print_response
def edit_file(_id, name, content):
    msg = {'name': name, 'content': content, 'your mom': 'glenna'}
    msg = {k: v for k, v in msg.items()}
    return requests.put(address + str(_id), json={'message': msg})


@print_response
def del_file(_id):
    return requests.delete(address + str(_id))


r = add_file('test_file_name.txt', 'HELO WORLD')
rj = r.json()

if 'created file' in rj and 'url' in rj['created file']:
    file_url = rj['created file']['url']
    print('fileurl', file_url)
    get_file_with_url(file_url)

get_file_with_id(1)
get_file_with_path(1)
edit_file(1, None, 'GOODBYE WORLD')
get_file_with_id(1)
del_file(1)
get_file_with_id(1)
