from generators import fake_data


class Data:
    @staticmethod
    def generate_user():
        email, password, name = fake_data()
        return {
            'email': email,
            'password': password,
            'name': name
        }


INGREDIENTS = [
    '61c0c5a71d1f82001bdaaa6c',
    '61c0c5a71d1f82001bdaaa74',
    '61c0c5a71d1f82001bdaaa78'
]
