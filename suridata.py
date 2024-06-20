import random
from multiprocessing import Process, Manager

from utils import get_list_of_employees, remove_duplicate_employees, get_gamad_anak

if __name__ == "__main__":
    employees: list = get_list_of_employees("data.json")
    employees_dedup: list = remove_duplicate_employees(employees)
    list_of_pairs: list = get_gamad_anak(employees_dedup)

    print("SINGLE PROCESS RESULT")
    print(list_of_pairs)

    ## Bonus
    random.shuffle(employees_dedup)  # so each time we'll have different liat_a and list_b
    list_a: list = employees_dedup[:int(len(employees_dedup) / 2)]
    list_b: list = employees_dedup[int(len(employees_dedup) / 2):]
    list_of_employees_lists: list = [list_a, list_b]

    processes = []
    manager = Manager()
    multi_process_shared_list = manager.list()
    for i in range(len(list_of_employees_lists)):
        process = Process(target=get_gamad_anak, args=(list_of_employees_lists[i], multi_process_shared_list))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    multi_process_combined_list = []
    for sublist in multi_process_shared_list:
        multi_process_combined_list.extend(sublist)

    print("MULTI-PROCESS PROCESS RESULT")
    print(multi_process_combined_list)
