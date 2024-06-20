import json
import random


def get_list_of_employees(path: str):
    with open(path) as file:
        data: list = json.load(file)
    return data


def remove_duplicate_employees(employees: list):
    employees_list = [json.dumps(employee, sort_keys=True) for employee in employees]
    unique_employees_list = list(set(employees_list))
    unique_employees_details = [json.loads(employee) for employee in unique_employees_list]
    return unique_employees_details


def get_gamad_anak(employees: list, shared_list=None):
    random.shuffle(employees)
    list_of_pairs: list = []
    for index, employee in enumerate(employees):
        if index == len(employees) - 1:
            pair = (employee["name"], employees[0]["name"])
        else:
            pair = (employee["name"], employees[index + 1]["name"])

        list_of_pairs.append(pair)

    if shared_list is not None:
        shared_list.append(list_of_pairs)

    return list_of_pairs

