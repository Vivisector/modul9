def double(x):
    return x*2

def triple(x):
    return x*3

def squared(x):
    return x*x

def max_(lst):
    return max(lst)

def min_(lst):
    return min(lst)

def len_(lst):
    return len(lst)

def sum_(lst):
    return sum(lst)

def sorted_(lst):
    return sorted(lst)

def apply_all_func_my(int_list, *functions):
    result = {}
    for n in int_list:
        for f in functions:
            result[f"{f.__name__} {n}"] = f(n)
    return result

def apply_all_func(int_list, *functions):
    result = {}
    for f in functions:
        result[f"{f.__name__}"] = f(int_list)
    return result

int_list = [6, 20, 15, 9]

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

# print('='*20)
print(f'{'\nфакультативные функции (мои) ':*^20}')
print(apply_all_func_my(int_list, double, triple, squared))
