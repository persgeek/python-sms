import requests

class Ghasedak:

    apiKey = None

    template = None
    receptor = None
    message = None
    token = None

    BASE_URL = 'https://api.ghasedak.me/v2'

    def __init__(self, apiKey):

        self.apiKey = apiKey

    def template(self, template):

        self.template = template

        return self

    def receptor(self, receptor):

        self.receptor = receptor
        
        return self

    def message(self, message):

        self.message = message

        return self

    def token(self, token):

        self.token = token

        return self

    class Response:

        response = None

        def __init__(self, response):

            self.response = response

        def json(self):

            return self.response.json()

        def success(self):

            if self.response.status_code in [200, 201]:
                return True

            return False

    def getSession(self):

        session = requests.session()

        headers = {
            'Accept': 'application/json',
            'apikey': self.apiKey
        }

        session.headers = headers

        return session

    def sendToken(self):

        url = self.getUrl('//verification/send/simple')

        data = {
            'receptor': self.receptor, 'message': self.message, 'param1': self.token, 'template': self.template, 'type': 1
        }

        response = self.getSession().post(url, data)

        return self.Response(response)

    def getUrl(self, *parts):

        url = self.BASE_URL

        for part in parts:

            url = self.append(url, '/', part)

        return url

    def append(self, *parts):

        output = ''

        for part in parts:

            output += str(part)

        return output