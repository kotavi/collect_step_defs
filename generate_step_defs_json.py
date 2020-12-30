import json


def collect_step_definition_files():
    import glob
    result = []
    for name in glob.glob('tests/step_defs/**/*step_definitions*.py', recursive=True):
        result.append(name)
    print(result)
    return result


def create_step_defs_dict(paths):
    result_dict = {}
    for path in paths:
        path_split = path.split('/')
        step_def_file_name = path_split[-1].split(".")[0]
        if len(path_split) == 3:
            result_dict[step_def_file_name] = {}
        elif len(path_split) > 3:
            screen_name = path_split[-2].split(".")[0]
            if screen_name not in result_dict:
                result_dict[screen_name] = {}
            if screen_name in result_dict:
                result_dict[screen_name][step_def_file_name] = {}
    return result_dict


def create_dict(paths):
    matches = ["@when", "@then", "@given"]
    result_dict = create_step_defs_dict(paths)
    for path in paths:
        path_split = path.split('/')
        store_description = False
        step_name, quotes = None, 0
        step_def_file_name = path_split[-1].split(".")[0]
        if len(path_split) == 3:
            # result_dict[step_def_file_name] = {}
            with open(path, 'r') as f:
                file_content = f.readlines()
            for line in file_content:
                if line.startswith("from") or line == '\n':
                    continue
                if any(x in line for x in matches):
                    quotes = 0
                    try:
                        step_name = line.split('\'')[1]
                    except Exception as e:
                        continue
                    if step_name not in result_dict[step_def_file_name]:
                        result_dict[step_def_file_name][step_name] = ""
                    continue
                if '"""' in line:
                    # quotes += 1
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
                    try:
                        result_dict[step_def_file_name][step_name.strip()] += (line.strip() + '\n')
                    except KeyError as ex:
                        print(ex)

        elif len(path_split) > 3:
            common_name = path_split[-2].split(".")[0]
            with open(path, 'r') as f:
                file_content = f.readlines()
            for line in file_content:
                if line.startswith("from") or line == '\n':
                    continue
                if any(x in line for x in matches):
                    quotes = 0
                    try:
                        step_name = line.split('\'')[1]
                    except IndexError as ex:
                        print(ex)
                        print(line)
                    if step_name not in result_dict[common_name][step_def_file_name]:
                        result_dict[common_name][step_def_file_name][step_name] = ""
                    continue
                if '"""' in line:
                    # quotes += 1
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
                    result_dict[common_name][step_def_file_name][step_name.strip()] += line.strip()
    return result_dict


def read_files(paths):
    for path in paths:
        with open(path, 'r') as f:
            file_content = f.readlines()
        for line in file_content:
            if "@when" in line:
                print(line)


print(create_step_defs_dict(collect_step_definition_files()))
print(create_dict(collect_step_definition_files()))

output = create_dict(collect_step_definition_files())
with open('data.json', 'w') as outfile:
    json.dump(output, outfile)