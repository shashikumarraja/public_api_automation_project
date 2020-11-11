
import pytest

from src.utils.api_utils import ApiUtils
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
        
    def test_status_code(self):
        endpoint = "facts"
        url = self.api_utils.build_url(endpoint)
        response = self.api_utils.get(url)
        assert response.status_code == 200, "Invalid response code:%s"% response.status_code