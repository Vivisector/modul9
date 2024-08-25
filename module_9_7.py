print('\n' + '* ' * 25)
print(f'{' УРОК 7 (Декораторы) ':*^49}')
print('* ' * 25 + '\n')

import random


def gen_args():
    args_ = []
    len_ = 3
    for i in range(len_):
        args_.append(random.randint(0, 20))
    return args_


def is_prime(func):
    def wrapper(*args):
        res_tmp = func(*args)
        # str = f'Число {res_tmp}: простое'
        str = f'простое\n{res_tmp}'
        for i in range(2, res_tmp + 1):
            if i < (res_tmp / 2) + 1:
                if res_tmp % i == 0:
                    str = f'составное\n{res_tmp}'
                    break
        return str

    return wrapper


@is_prime
def sum_three(*args):
    return (sum(args))


print('Примеры проверок:')
for _ in range(4):
    result = sum_three(*gen_args())
    print(result)
    print('-' * 10)  # decor
print('Числа из домашнего задания <2, 3, 6>:')
result = sum_three(2, 3, 6)
print(result)
# result = sum_three(2, 3, 6, 9)
# print(result)
# result = sum_three(2, 3, 4, 8)
# print(result)
