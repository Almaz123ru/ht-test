import json
import sys

path1 = sys.argv[1]
path2 = sys.argv[2]
path3 = sys.argv[3]


def parse_json(data):
    if isinstance(data, list):
        arr = []
        for val in data:
            arr.append(parse_json(val))
        return arr
    elif isinstance(data, dict):
        result = {}
        for key, val in data.items():
            if key == "id":
                emp_id = val
            if key == "value":
                for item in values['values']:
                    for key_val, val_val in item.items():
                        if val_val == emp_id:
                            result[key] = val_val
            else:
                result[key] = parse_json(val)
        return result
    else:
        return data


with open(path1, encoding="UTF-8") as file_in:
    values = json.load(file_in)

with open(path2, encoding="UTF-8") as file_in:
    tests = json.load(file_in)

parsed_json = parse_json(tests)

with open(path3, "w", encoding="UTF-8") as file_out:
    json.dump(
        parsed_json,
        file_out,
        indent=2
    )
