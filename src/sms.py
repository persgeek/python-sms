import requests

class SMS:

    apiKey = None
    secretKey = None

    def __init__(self, apiKey, secretKey):
        self.apiKey = apiKey
        self.secretKey = secretKey

    def getToken(self):

        url = 'https://restfulsms.com/api/Token'

        headers = {
            'Content-Type': 'application/json'
        }

        params = {
            'UserApiKey': self.apiKey,
            'SecretKey': self.secretKey
        }

        response = requests.post(url, headers=headers, json=params)

        return response.json()

    def sendOTP(self, token, phone, code):

        url = 'https://restfulsms.com/api/VerificationCode'

        headers = {
            'Content-Type': 'application/json',
            'x-sms-ir-secure-token': token
        }

        params = {
            'Code': code,
            'MobileNumber': phone
        }

        response = requests.post(url, headers=headers, json=params)

        return response.json()
