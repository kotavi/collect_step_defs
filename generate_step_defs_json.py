import json
from functools import reduce
import operator
import xlsxwriter


def collect_step_definition_files():
    """
    :return: a list of all paths with *step_definitions*.py in filename
    """
    import glob
    result = []
    for name in glob.glob('tests/step_defs/**/*step_definitions*.py', recursive=True):
        result.append(name)
    return result


def create_step_defs_dict(paths):
    """

    :param paths: a list of paths
    :return: dictionary
    e.g. {"folder_name1": {"folder_name2": {"step_definition_file_name": {}}}}

    Issue:
        Should be done recursively
    """
    tree = {}
    for path in paths:
        node = tree
        new_path = path.split('/')[2:]
        for level in new_path:
            if level:
                if '.py' in level:
                    level = level.split('.')[0]
                node = node.setdefault(level, dict())  # move to a deeper level (or create it if doesn't exist)
    return tree


def get_from_dict(data_dict, map_list):
    return reduce(operator.getitem, map_list, data_dict)


def set_in_dict(data_dict, map_list, value):
    get_from_dict(data_dict, map_list[:-1])[map_list[-1]] = value


def create_dict(paths):
    matches = ["@when", "@then", "@given"]
    result_dict = create_step_defs_dict(paths)
    print(result_dict)
    for path in paths:
        with open(path, 'r') as f:
            file_content = f.readlines()
        path_split = path.split('/')[2:]
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


output = create_dict(collect_step_definition_files())
with open('data.json', 'w') as outfile:
    json.dump(output, outfile)

path_split = []
workbook = xlsxwriter.Workbook('StepDefinitions.xlsx')
wrap_format = workbook.add_format({'text_wrap': 1, 'valign': 'vcenter'})
cell_format = workbook.add_format({'bold': True})
cell_format.set_bg_color('#fdf7e6')

for path in collect_step_definition_files():
    path_split = path.split('/')[2:]
    step_def_file_name = path_split[-1].split(".")[0]
    path_split[-1] = step_def_file_name
    step_definitions = get_from_dict(output, path_split)

    worksheet = workbook.add_worksheet(name=step_def_file_name.split('_step_')[0])
    step_definitions = [
        [key, value] for key, value in step_definitions.items()
    ]

    # Start from the first cell. Rows and columns are zero indexed.
    row, col = 1, 0
    worksheet.set_column(0, 0, 50)
    worksheet.set_column(1, 1, 100)
    worksheet.write(0, 0, "Path to step definition file: \n%s" % path, cell_format)
    worksheet.write(0, 1, "", cell_format)
    worksheet.add_table(2, 0, len(step_definitions) + 2, 1,
                        {'data': step_definitions,
                         'columns': [
                             {'header': 'Step Name', 'format': wrap_format},
                             {'header': 'Definition', 'format': wrap_format}]
                         })

workbook.close()
