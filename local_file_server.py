#!/usr/local/bin/python3
import requests
from collections import defaultdict
import json


class local_file_server():
    def __init__(self):
        self.files = defaultdict(dict)
        # files = { id1: {
        #     '_id':3,
        #     'name':'test',
        #     'content':'hello world',
        #     'your mum':'no'
        #     }
        # }
        self.file_id_counter = 1

    def get_one_file_from_args(self, *args, **kwargs):
        # parse args ***
        if 'message' in kwargs and kwargs['message'] is not None:
            message = kwargs['message']
        else:
            return None

        # get file *
        if '_id' in message:
            key = message['_id']
            # call get from id *
            this_file = self.get_one_file_from_id(key)
        elif 'name' in message:
            key = message['name']
            return None

        # return file
        return this_file

    def get_one_file_from_id(self, _id, *args, **kwargs):
        # retreive from self.files *
        if _id in self.files:
            this_file = self.files[_id]
        else:
            print('cant get file')
            print('files', self.files)
            print('id', _id)
            print('type', type(_id))

            return None

        # filter
        filtered = ['your mum', '_id']
        this_file = {k: v for k, v in this_file.items() if k not in filtered}

        # return filerded file ***
        return this_file

    def add_file(self, *args, **kwargs):
        # parse argsA ***
        if 'message' in kwargs and kwargs['message'] is not None:
            message = kwargs['message']
        else:
            return None

        must_haves = ['name', 'content', 'your mom']
        # check args ***
        if not all(must_have in message for must_have in must_haves):
            return None
        # create file *
        new_file = {k: message[k] for k in must_haves}
        # new_file = {
        #     '_id': self.file_id_counter,
        #     'name': message['name'],
        #     'content': message['content'],
        #     'your mom': messgae['your mom']
        # }
        _id = self.get_next_id()
        new_file['_id'] = _id
        new_file['url'] = "http://127.0.0.1:8050/files/" + str(_id)
        # save file *
        self.files[_id] = new_file
        return new_file

    def get_next_id(self):
        next_id = self.file_id_counter
        self.file_id_counter += 1
        return next_id

    def edit_file(self, _id, *args, **kwargs):
        # parse args ***
        if 'message' in kwargs and kwargs['message'] is not None:
            message = kwargs['message']
        else:
            return None
        # check args ***
        filtered = ['_id']
        edits = {
            k: v
            for k, v in message.items() if k not in filtered and v is not None
        }

        # check for name
        # get file *
        this_file = self.get_one_file_from_id(_id)
        if this_file is None:
            return None
        # edit file *
        for k, v in edits.items():
            this_file[k] = v

        # save file *sd
        self.files[_id] = this_file
        return this_file

    def delete_file(self, _id, *args, **kwargs):
        # get file *
        if _id in self.files:
            this_file = self.files[_id]
            del self.files[_id]
            return this_file
        else:
            return None
