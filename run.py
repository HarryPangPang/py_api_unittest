import pytest
from helper import get_data_from_sheet, get_excel, get_excel_path


class StartTest:

	def __init__(self) -> None:
	    pass

	def run(self):
		print('开始测试')
		# cases = get_excel("sdk", "cases.xls", "unified_api")
		# for case in cases:
		# 	print(case[0])
		pytest.main(["-q", "--html=report/report.html"])


if __name__ == '__main__':
    StartTest().run()
