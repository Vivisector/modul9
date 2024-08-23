first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
#############
first_res = [len(s) for s in first_strings if len(s) > 4]
first_res_dicted = {s: len(s) for s in first_strings if len(s) > 4}
print()
print(f'{' first ':*^25}')
print(f'Длины строк длинее 4 символов: {list(first_res)}')
print(first_res_dicted, end='\n\n')
##############
print(f'{' second (кортежные пары из строк одинаковой длины) ':*^65}')
second_res = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]
# кортежный список (с доп. указанием количества символов)
second_res_len = [(len(s1), s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]
print(*second_res)
print(f'{' second (пары из строк одинаковой длины c указанием длины) ':*^73}')
print(*second_res_len, end='\n\n')
##############
# third_res_full = [(len(s1), s1, len(s2), s2) for s1 in first_strings for s2 in second_strings]
# third_res_even = [(len(s1), s1, len(s2), s2) for s1 in first_strings for s2 in second_strings if
#                    not len(s1) % 2 and not len(s2) % 2]
third_res_joined = {s: len(s) for s in first_strings + second_strings}
third_res_joined_even = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}
print(f'{' third (выборка из объединенных списков) ':*^55}')
print('все строки:')
print(third_res_joined)
print('строки c четной длиной:')
print(third_res_joined_even)
