import time as tm
import random as rm

def is_sorted(lst: list[int]):
    return lst == sorted(lst)

def boggo_sort_power(input_list: list[int], input_list_len: int, sorted_list: list[int], power: int = 1) -> None:
    while True:
        return_list: list = []
        for i in range(power):
            return_list.append(rm.sample(input_list, input_list_len))
        if all([return_list[i] == sorted_list for i in range(len(return_list))]):
            return None

def boggo_sort_linear(input_list: list[int], input_list_len: int, sorted_list: list[int], counter: int = 1) -> None:
    while True:
        return_list: list = []
        for i in range(counter):
            return_list.append(rm.sample(input_list, input_list_len))
        if not all([return_list[i] == sorted_list for i in range(len(return_list))]):
            counter += 1
            continue
        return None

def thanos_sort(input_list: list[int]) -> tuple[list[int], int]:
    while not is_sorted(input_list):
        input_list = input_list[:len(input_list)//2] if rm.randint(0, 1) == 0 else input_list[len(input_list)//2:]
    return input_list, len(input_list)

def main() -> None:
    input_list: list[int] = [3, 1, 2, -1, 4, 7]
    input_list_len: int = len(input_list)
    sorted_list: list[int] = sorted(input_list)
    power: int = rm.randint(1, 99999)
    counter: int = 1
    algorithm: int = 0

    if algorithm == 0:
        initial_time = tm.perf_counter()
        boggo_sort_power(input_list=input_list, input_list_len=input_list_len, sorted_list=sorted_list, power=power)
        print(f"Boggo_sort_power took: {tm.perf_counter() - initial_time}s to sort a list of {input_list_len} elements.")

    elif algorithm == 1:
        initial_time = tm.perf_counter()
        boggo_sort_linear(input_list=input_list, input_list_len=input_list_len, sorted_list=sorted_list, counter=counter)
        print(f"Boggo_sort_linear took: {tm.perf_counter() - initial_time}s to sort a list of {input_list_len} elements.")

    elif algorithm == 2:
        initial_time = tm.perf_counter()
        results: tuple[list[int], int] = thanos_sort(input_list=input_list)
        print(f"Thanos_sort took: {tm.perf_counter() - initial_time}s to sort a list of {input_list_len} elements but reduced it to {results[0]} of len {results[1]}.")

if __name__ == '__main__':
    main()
