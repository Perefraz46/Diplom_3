import requests
import url


class UserService:
    @staticmethod
    def register_user(user_data):
        return requests.post(f'{url.MAIN_PAGE_URL}{url.REGISTRATION}', json=user_data)

    @staticmethod
    def delete_user(auth_token):
        return requests.delete(f'{url.MAIN_PAGE_URL}{url.DELETE}', headers={'Authorization': auth_token})
