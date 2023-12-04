import multiprocessing


# result = []
# def calc_square(numbers):
#     global result
#     for num in numbers:
#         result.append(num * num)
#     print("inside res", result)

# if __name__ == '__main__':
#     numbers = [1,3,4]
#     p = multiprocessing.Process(target=calc_square, args=(numbers,))
#     p.start()
#     p.join()

#     print('outside process', result)

"""
inside res [1, 9, 16]
outside process []

outside process is empty because if new process is created a separate address space will create for that process
"""


def calc_square(numbers, result, v):
    print(v.value)
    v.value = 0.56
    for idx, num in enumerate(numbers):
        result[idx] = (num * num)
    print("inside res", result[:])

if __name__ == '__main__':
    numbers = [1,3,4]
    #shared memory for array
    result = multiprocessing.Array('i',3)
    v = multiprocessing.Value('d',0.89)
    p = multiprocessing.Process(target=calc_square, args=(numbers,result,v))
    p.start()
    p.join()

    print('outside process', result[:])
    print(v.value)

"""
0.89
inside res [1, 9, 16]
outside process [1, 9, 16]
0.56
"""