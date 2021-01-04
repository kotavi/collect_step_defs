import json
from functools import reduce
import operator


def collect_step_definition_files():
    import glob
    result = []
    for name in glob.glob(r'tests\step_defs\**\*step_definitions*.py', recursive=True):
        result.append(name)
    return result


def create_step_defs_dict(paths):
    tree = {}
    for path in paths:
        node = tree
        new_path = path.split('\\')[2:]
        for level in new_path:
            if level:  # if a name is non-empty
                if '.py' in level:
                    level = level.split('.')[0]
                node = node.setdefault(level, dict())  # move to the deeper level (or create it if doesn't exist)
    return tree


def get_from_dict(data_dict, map_list):
    return reduce(operator.getitem, map_list, data_dict)


def set_in_dict(data_dict, map_list, value):
    get_from_dict(data_dict, map_list[:-1])[map_list[-1]] = value


def create_dict(paths):
    matches = ["@when", "@then", "@given"]
    result_dict = create_step_defs_dict(paths)
    for path in paths:
        with open(path, 'r') as f:
            file_content = f.readlines()
        path_split = path.split('\\')[2:]
        step_def_file_name = path_split[-1].split(".")[0]
        path_split[-1] = step_def_file_name
        store_description = False
        step_name, quotes = None, 0

        path_content = {}
        for line in file_content:
            if line.startswith("from") or line == '\n':
                continue
            if any(x in line for x in matches):
                quotes = 0
                step_name = line.split('\'')[1]
                dict_path = get_from_dict(result_dict, path_split)
                if step_name not in dict_path:
                    path_content[step_name] = ""
                continue
            if '"""' in line:
                if store_description:
                    store_description = False
                    step_name = None
                    quotes = 0
                    continue
            if step_name and '"""' in line:
                store_description = True
                quotes += 1
                continue
            if store_description and '"""' not in line:
                path_content[step_name] += (line.strip() + '\n')
        set_in_dict(result_dict, path_split, path_content)
    return result_dict


def read_files(paths):
    for path in paths:
        with open(path, 'r') as f:
            file_content = f.readlines()
        for line in file_content:
            if "@when" in line:
                print(line)


output = create_dict(collect_step_definition_files())
with open('data.json', 'w') as outfile:
    json.dump(output, outfile)

