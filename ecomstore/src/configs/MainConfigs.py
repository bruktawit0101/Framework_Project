

import os

class MainConfigs:

    URL_CONFIGS = {
        "dev": {
            "base_url": "dev.http://localhost:8888/quicksite/"
        },
        "test": {
            "base_url": "http://localhost:8888/quicksite/"
        },
        "staging": {
        },
        "prod": {
        }
    }


    @staticmethod
    def get_base_url():

        base_url = os.environ.get('BASE_URL')

        if not base_url:
            environment = os.environ.get("ENV", "test")

            return MainConfigs.URL_CONFIGS[environment.lower()]['base_url']

        else:
            return base_url

    @staticmethod
    def get_coupon_code(filter):
        if filter.upper() == 'FREE_COUPON':
            return 'SSQA100'

        else:
            raise Exception(f"Unknown value for parameter 'filter. filter={filter}")


