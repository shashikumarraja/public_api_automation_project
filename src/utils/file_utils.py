"""
Utils to perform file related operation
"""
import json
import os

from src.utils.logger_utils import CustomLogger

LOG = CustomLogger.getLogger(__name__)


class FileUtils():

    def create_dir(self, path):
        """Create a directory

        Args:
            path (string): folder path to create

        Raises:
            err: OSError 
        """
        try:
            os.makedirs(path, exist_ok=True)
        except OSError as err:
            LOG.error("Creation of the directory: %s failed", path)
            raise err
        else:
            LOG.info("Successfully created the directory: %s", path)

    def is_file(self, file_path):
        """Checks if a path is valid file

        Args:
            file_path (string):

        Returns:
            boolean:
        """
        return os.path.isfile(file_path)

    def get_file_size(self, file_path):
        """Returns the file size

        Args:
            file_path (string):

        Returns:
            integer:
        """
        return os.path.getsize(file_path)

    def is_non_empty_file(self, file_path):
        """Checks if file is non empty

        Args:
            file_path (string): path to check file content

        Returns:
            boolean:
        """
        return self.is_file(file_path) and self.get_file_size(file_path) > 0

    def is_valid_json(self, json_data):
        """Checks whether data is valid json or not

        Args:
            json_data (json): data to validate

        Returns:
            boolean:
        """
        try:
            json_object = json.loads(json_data)
        except ValueError as err:
            LOG.error("Invalid json: %s" % err)
            return False
        return True

    def get_json_content(self, file_path):
        """Get json content from file

        Args:
            file_path (string): path to read data from

        Returns:
            json:
        """
        content = {}
        try:
            if self.is_non_empty_file(file_path):
                with open(file_path, 'r') as f:
                    content = json.load(f)
            else:
                LOG.debug("Input file not available for reading: %s", file_path)
        except Exception as err:
            LOG.debug("Exception caught while loading json file: %s,"
                      "Exception: %s" % (file_path, err))
            raise err
        return content
