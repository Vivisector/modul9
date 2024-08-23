first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

zip_ = list(zip(first, second))
# print(*zip_)
print()
print(f'{" first ":*^25}')
# first_res= (abs(len(f)-len(s)) for f in first for s in second if len(f)-len(s)!=0)
first_res_zipped= (abs(len(s[0])-len(s[1])) for s in zip_ if len(s[0])-len(s[1])!=0)
# print(*first_res)
print(*first_res_zipped, end = '\n\n')
print(f'{" second ":*^25}')
###########
# for i in range(len(first)):
#     print(len(first[i]) - len(second[i]))

second_res_true = (len(first[i])==len(second[i]) for i in range(len(first)))
print('*** сборка с True/False ***')
print(*second_res_true)
second_res = ((abs(len(first[i])-len(second[i]))) for i in range(len(first)))
print('*** сборка с числовой разницей ***')
print(*second_res)
