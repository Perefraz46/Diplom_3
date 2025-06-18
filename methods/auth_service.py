import requests
import url


class AuthService:
    @staticmethod
    def get_auth_token(credentials):
        response = requests.post(f'{url.MAIN_PAGE_URL}{url.LOGIN}', json=credentials)
        return response.json()['accessToken']
