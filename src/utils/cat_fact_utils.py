"""Utils for cat fact api
"""
from src.utils.api_utils import ApiUtils
from src.utils.logger_utils import CustomLogger

LOG = CustomLogger.getLogger(__name__)


class CatFactUtils():
    def __init__(self, hostname=None):
        self.api_utils = ApiUtils(hostname=hostname, is_https=True)

    def get_all_facts(self):
        LOG.info("calling all facts api")
        headers_dict = {
            "Accept": "*/*",
            "Content-Type": "application/json"
        }
        all_facts_path = "facts"
        url = self.api_utils.build_url(all_facts_path)
        response = self.api_utils.get(url, headers=headers_dict)
        return response

    def get_random_fact(self, animal_type=None, amount=None):
        LOG.info("calling random fact api")
        random_fact_path = "facts/random"
        headers_dict = {
            "Accept": "*/*",
            "Content-Type": "application/json"
        }
        params_dict = {}
        if animal_type:
            params_dict["animal_type"] = animal_type
        if amount:
            params_dict["amount"] = amount
        url = self.api_utils.build_url(random_fact_path)

        response = self.api_utils.get(url, headers=headers_dict) if not params_dict else self.api_utils.get(
            url, headers=headers_dict, params_dict=params_dict)
        return response
