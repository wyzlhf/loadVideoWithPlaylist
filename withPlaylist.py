import os


def get_list_video(path, url):
    command_word = 'you-get --playlist ' + url + ' -o ' + path
    os.system(command_word)


if __name__ == '__main__':
    path = r'D:\Video\2020年数据库设计和编程'
    url = 'https://www.bilibili.com/video/BV1fk4y1B7ah'
    get_list_video(path, url)
