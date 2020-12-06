import json


def process_arr(arr):
    ans = 0
    for x in arr:
        if isinstance(x, int):
            ans += x
        elif isinstance(x, list):
            ans += process_arr(x)
        elif isinstance(x, dict):
            ans += process_obj(x)
    return ans


def process_obj(obj):
    ans = 0
    for k, v in obj.items():
        if isinstance(v, int):
            ans += v
        elif isinstance(v, dict):
            ans += process_obj(v)
        elif isinstance(v, list):
            ans += process_arr(v)
    return ans


data = json.load(open('in'))
print(process_obj(data))
