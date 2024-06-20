import random
from multiprocessing import Process

from utils import get_list_of_employees, remove_duplicate_employees, get_gamad_anak, get_process_worker_id

if __name__ == "__main__":
    employees: list = get_list_of_employees("data.json")
    employees_dedup: list = remove_duplicate_employees(employees)
    list_of_pairs: list = get_gamad_anak(employees_dedup)

    ## Bonus
    random.shuffle(employees_dedup)  # so each time we'll have different liat_a and list_b
    list_a: list = employees_dedup[:int(len(employees_dedup) / 2)]
    list_b: list = employees_dedup[int(len(employees_dedup) / 2):]
    list_of_employees_lists: list = [list_a, list_b]

    processes = []
    for i in range(len(list_of_employees_lists)):
        process = Process(target=get_gamad_anak, args=(list_of_employees_lists[i],))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
