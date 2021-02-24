import os
from httprunner.api import HttpRunner
from httprunner.report import gen_html_report
import time

# 1、创建HttpRunner对象
# failfast当用例执行失败之后,会自动暂停,默认为False,可以不写
runner = HttpRunner(failfast=False, log_level='INFO')
run_report_path=r"reports/"+time.strftime('%Y%m%d%H%M%S')+".html"
# 2、运行用例
# run方法支持如下参数:
# yml用例文件的路径
# 字典(用例的信息)
#runner.run('testsuites/')
#gen_html_report(runner._summary, report_template="templates/extent-theme-template.html")

summary=runner.run(r'testsuites',dot_env_path='conf/env/.online_zy.env')
gen_html_report(summary,report_file=run_report_path)
print("报告地址:",os.path.abspath('.')+'/'+run_report_path)
#print(runner.summary)

