import unittest, time

from HTMLTestRunner import HTMLTestRunner


def suites(str_dri):

    caseSuites = unittest.TestSuite()

    discover = unittest.defaultTestLoader.discover(str_dri, pattern="*.py", top_level_dir=str_dri)
    caseSuites.addTest(discover)

    return caseSuites


def main(str_dri):
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    fileName = "../report/" + now + ".html"

    with open(fileName, "wb") as files:
        runer = HTMLTestRunner(stream=files, title="测试报告", description="豆瓣项目")

        runer.run(suites(str_dri))
    files.close()


if __name__ == "__main__":
    main("../page/")
