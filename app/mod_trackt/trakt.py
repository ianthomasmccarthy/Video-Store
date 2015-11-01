#!flask/bin/python
import getpass
import base64
import json
import requests
from requests.auth import HTTPBasicAuth
import argparse
import re

class Auth:
    def __init__(self, user, __pword):
        self.user = user
        self.__pword = __pword
        self.url = 'https://mtjira.searshc.com/jira/rest/auth/1/session'
        self.cookie_key = 'JSESSIONID'
        self.cookie = ''
        self.authenticate()
        self.write_cookie_file()

    def authenticate(self):
        payload = {
                    "username": self.user,
                    "password": self.__pword
                  }
        request = requests.Session()
        data = request.post(self.url,
                            auth=HTTPBasicAuth(self.user, self.__pword),
                            data=json.dumps(payload),
                            verify=False)

        self.cookie = data.cookies[self.cookie_key]

    def write_cookie_file(self):
        filename = '''cookies/{user}.cookie'''.format(user=self.user)
        with open(filename, 'w') as f:
            f.write(self.cookie)

class Rest:
    def __init__(self, user, __pword):
        self.user     = user
        self.__pword  = __pword
        self.base_url = 'https://mtjira.searshc.com/jira/rest/api/2/'

    def get(self, uri):
        url = self.base_url + uri
        headers = {"Content-type": "application/json"}
        request = requests.get(url,
                                auth=HTTPBasicAuth(self.user,
                                self.__pword),
                                headers=headers,
                                verify=False)

        return request.text

    def post(self, uri, payload=''): 
        url = self.base_url + uri
        headers = {"Content-type": "application/json"}
        request = requests.post(url,
                                auth=HTTPBasicAuth(self.user,
                                self.__pword),
                                data=json.dumps(payload),
                                headers=headers,
                                verify=False)

        return request.text

    def put(self, uri, payload=''):
        url = self.base_url + uri
        headers = {"Content-type": "application/json"}
        request = requests.put(url,
                               auth=HTTPBasicAuth(self.user, self.__pword),
                               data=json.dumps(payload),
                               headers=headers,
                               verify=False)
        return request.text



if __name__ == '__main__':
	runit()