from urllib.request import urlopen
for line in urlopen('http://www.cnblogs.com/qb371/archive/2011/10/12/2366294.html'):
    line = line.decode('utf-8') #look for eastern time
    if '空间参考' in line:  #look for eastern time
        print(line)