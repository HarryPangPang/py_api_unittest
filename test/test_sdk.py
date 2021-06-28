import json
import pytest
from helper import get_data_from_sheet, get_excel_path
from cus_http import sdk

@pytest.mark.parametrize(*get_data_from_sheet(get_excel_path("sdk", "cases.xls"), "unified_api" ))
def test_request(name,path,query, method):
	result =  sdk.sdk_post(path, query)
	assert result