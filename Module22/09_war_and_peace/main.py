import collections
import zipfile


def unzip(archive):
    with zipfile.ZipFile(archive, 'r') as filezip:
        for file in filezip.namelist():
            filezip.extract(file)
    filezip.close()


def stats(file_name):
    res = {}
    if file_name.endswith('.zip'):
        unzip(file_name)
        file_name = ''.join((file_name[:-3], 'txt'))
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            for sym in line:
                if sym.isalpha():
                    if sym not in res:
                        res[sym] = 0
                    res[sym] += 1
        file.close()
    sort_res = sorted(res.values(), reverse=True)
    sort_dict = collections.OrderedDict()
    for value in sort_res:
        for key in res.keys():
            if res[key] == value:
                sort_dict[key] = res[key]
    return sort_dict


result = stats('voyna-i-mir.zip')

for k, v in result.items():
    print(k, v)
