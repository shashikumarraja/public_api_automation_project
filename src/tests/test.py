
import pytest

from src.utils.api_utils import ApiUtils
from src.utils.cat_fact_utils import CatFactUtils
from src.validators.validators import Validators
from src.utils.data_utils import DataUtils
from src.utils.logger_utils import CustomLogger

LOG = CustomLogger.getLogger(__name__)


@pytest.mark.cat_fact
class TestCatFact:
    """
    Test Class for testing CatFact Apis
    """
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        request.cls.base_url = request.config.base_url
        request.cls.api_utils = ApiUtils(hostname=self.base_url, is_https=True)
        request.cls.cat_fact_utils = CatFactUtils(hostname=self.base_url)
        request.cls.validator = Validators()
        request.cls.data_utils = DataUtils()
        request.cls.all_facts_schema = self.data_utils.get_all_facts_schema()
        request.cls.single_fact_schema = self.data_utils.get_single_fact_schema()
        request.cls.multi_facts_schema = self.data_utils.get_multiple_facts_schema()

    def test_get_all_facts(self):
        response = self.cat_fact_utils.get_all_facts()

        # validate status code
        assert response.status_code == 200, "Invalid response code:%s" % response.status_code

        # validate response schema
        response_json = self.api_utils.get_resp_json(response)
        self.validator.assert_valid_schema(
            response_json, self.all_facts_schema)

    def test_get_random_fact(self):
        response = self.cat_fact_utils.get_random_fact()

        # validate status code
        assert response.status_code == 200, "Invalid response code:%s" % response.status_code

        # validate response schema
        response_json = self.api_utils.get_resp_json(response)
        self.validator.assert_valid_schema(
            response_json, self.single_fact_schema)

    def test_get_random_fact_with_valid_query_params(self):
        animal_type = self.data_utils.get_random_valid_animal_type()
        amount = self.data_utils.get_random_number(min_value=1, max_value=500)
        response = self.cat_fact_utils.get_random_fact(
            animal_type=animal_type, amount=amount)

        # validate status code
        assert response.status_code == 200, "Invalid response code:%s" % response.status_code

        # validate response schema
        response_json = self.api_utils.get_resp_json(response)
        if amount > 1:
            self.validator.assert_valid_schema(
                response_json, self.multi_facts_schema)
        else:
            self.validator.assert_valid_schema(
                response_json, self.single_fact_schema)
