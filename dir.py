# -*-coding:utf-8 -*-
import os

dir = "D:\\pixelHeroes\\output\\game_asset\\assets\\src"

# 遍历文件夹
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s\\%s' % (filepath, allDir))
        # 以.lua结尾的文件
        if os.path.isfile(child):
            if child.endswith(".lua"):
                print(child)
        else:
            eachFile(child)

# 入口
if __name__ == '__main__':
    eachFile(dir)