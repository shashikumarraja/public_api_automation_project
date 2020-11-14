"""Util to generate test data
"""
from faker import Faker
from src.utils.logger_utils import CustomLogger

LOG = CustomLogger.getLogger(__name__)


class DataUtils():
    def __init__(self):
        self.faker = Faker()

    def get_random_string(self, min_chars=None, max_chars=10):
        """Generates a random size string

        Args:
            min_chars (int, optional): min number of chars. Defaults to None.
            max_chars (int, optional): max chars in string. Defaults to 10.

        Returns:
            str:
        """
        return self.faker.pystr(min_chars=min_chars, max_chars=max_chars)

    def get_random_number(self, min_value=0, max_value=9999):
        """Generates a random integer

        Args:
            min_value (int, optional): min val of integer. Defaults to 0.
            max_value (int, optional): max val of integer. Defaults to 9999.

        Returns:
            int:
        """
        return self.faker.pyint(min_value=min_value, max_value=max_value)

    def get_all_facts_schema(self):
        return "all_facts.json"

    def get_multiple_facts_schema(self):
        return "multiple_facts.json"

    def get_single_fact_schema(self):
        return "single_fact.json"
