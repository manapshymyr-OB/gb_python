import os

directory = r'my_project1'
groups = [100, 1000, 10000, 100000]
result = dict.fromkeys(groups, 0)

for path_from_top, subdirs, files in os.walk(directory):
    for file in files:
        path = os.path.join(path_from_top, file)
        size = os.path.getsize(path)
        to_group = min(filter(lambda x: size < x, groups))
        result[to_group] += 1

print(result)