import speedtest
import datetime

path = 'Data.txt'


def test():
    s = speedtest.Speedtest(secure=True)
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]


def write():
    d, u, p = test()
    data = '-----{}-----\n'.format(datetime.datetime.now())
    data += 'Download: {:.2f} Kb/s\n'.format(d / 1024)
    data += 'Upload: {:.2f} Kb/s\n'.format(u / 1024)
    data += 'Ping: {}\n'.format(p)
    data += '------------------------------------\n'
    file1 = open(path, "a")
    file1.write(data)
    file1.close()


if __name__ == '__main__':
    write()
