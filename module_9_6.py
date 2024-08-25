print('\n' + '* ' * 25)
print(f'{' УРОК 6 (Генераторы) ':*^49}')
print('* ' * 25)

def all_variants(text):
    for start in range(len(text)):
        for end in range(start+1, len(text) +1):
            yield text[start:end]

def all_variants2(text):
    length = len(text)
    for sub_len in range(1, length+1):
        for start in range(length - sub_len+1):
            yield text[start:start+sub_len]


a = all_variants('abc')
for i in a:
    print(i)

print('\n' + f'{' вывод в виде, показаном в ДЗ ':*^40}')
a = all_variants2('abc')
for i in a:
    print(i)