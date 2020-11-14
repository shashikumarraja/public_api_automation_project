"""
Helps in validating the tests
"""

import json
from os.path import dirname, join

from jsonschema import validate
from src.utils.logger_utils import CustomLogger

LOG = CustomLogger.getLogger(__name__)


class Validators():
    def load_schema(self, schema_filename):
        """Loads a json schema from given path

        Args:
            schema_filename (string): 

        Raises:
            err: [description]

        Returns:
            json:
        """
        schema_path = join(dirname(__file__), join('schemas', schema_filename))
        try:
            with open(schema_path) as schema_file:
                return json.loads(schema_file.read())
        except Exception as err:
            LOG.error(err)
            raise err

    def assert_valid_schema(self, json_response, schema_filename):
        """Validate the response with schema file

        Args:
            json_response (json):
            schema_filename (str): 

        Returns:
            bool:
        """
        schema = self.load_schema(schema_filename)
        return validate(json_response, schema)
