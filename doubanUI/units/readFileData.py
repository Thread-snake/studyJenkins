# -*- coding:utf-8 -*-
import csv
from collections import namedtuple


class fileData:

    def getData(self, fileName):

        with open(fileName, "r", encoding="utf-8-sig") as files:
            data = csv.reader(files)
            #next获取文件的第一行和第一列（获取标题）
            fileTuple = namedtuple("fileTuple", next(data))
            dataList = []
            for i in data:
                ft = fileTuple(*i)
                dataList.append(ft)

            return dataList

        files.close()


if __name__ == "__main__":
    print(fileData().getData("../resource/loginXpath.csv"))

