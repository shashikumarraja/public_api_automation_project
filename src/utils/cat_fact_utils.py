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
