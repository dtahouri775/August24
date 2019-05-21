import unittest
import nose
from calls import get_data
from mock import MagicMock
from mock import Mock, patch
import requests
class TestCalls(unittest.TestCase):
    def test_get_data(self):
        with patch.object(requests,'get')as get_mock:
            get_mock.return_value = mock_response = Mock()
            mock_response.status_code=200
            print(get_data())
            assert get_data()==200


if __name__ == "__main__":
    # unittest.main()
    nose.main()