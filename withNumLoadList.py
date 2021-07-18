import os


def get_video_with_num(path, url,endNum,startNum=1):
    for num in range(startNum,endNum+1):
        exec_command='you-get ' + url+'?p=' +str(num)+ ' -o ' + path
        os.system(exec_command)
if __name__ == '__main__':
    path = r'D:\Video\2020年数据库设计和编程'
    url = 'https://www.bilibili.com/video/BV1fk4y1B7ah'
    startNum=69
    endNum=70
    get_video_with_num(path, url,endNum,startNum)