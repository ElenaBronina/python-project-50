import json

def to_lower(str_):
    return str(str_).lower()

def diff(file1, file2):
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))
    diff = []
    for key in sorted(data1.keys() | data2.keys()):
        if key in data1 and key in data2 and data1[key] == data2[key]:
            diff.append(f'  {key}: {to_lower(data1[key])}')
        elif key in data1 and key in data2 and data1[key] != data2[key]:
            diff.append(f'- {key}: {to_lower(data1[key])}')
            diff.append(f'+ {key}: {to_lower(data2[key])}')
        elif key in data1:
            diff.append(f'- {key}: {to_lower(data1[key])}')
        elif key in data2:
            diff.append(f'+ {key}: {to_lower(data2[key])}')
    diff_list = "\n ".join(diff)
    return f'{{\n {diff_list}\n}}'
