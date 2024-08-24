from random import choice
print()
print(f'{' lambda ':*^20}')
first = 'Мама мыла раму'
second = 'Рамена мало было'
res = list(map(lambda x, y: x == y, first, second))
print('res:')
print(res)
print('в задании:')
print('[False, True, True, False, False, False, False, False, True, False, False, False, False, False]\n')

print(f'{' closure ':*^25}')
print('см. файлы example1, example2\n')

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as f:
            for item in data_set:
                f.write(str(item) + '\n')
            # f.write('===========\n')

    return write_everything


def get_advanced_writer_advanced(file_name): #разносим по строкам и второй элемент (список)
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as f:
            for item in data_set:
                if isinstance(item, list):
                    for i in item:
                        f.write(str(i) + '\n')
                else:
                    f.write(str(item) + '\n')

    return write_everything


write1 = get_advanced_writer('example.txt')
write2 = get_advanced_writer_advanced('example2.txt')
write1('Это отдельная строка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
write2('Это отдельная строка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


print(f'{' call_method ':*^20}')
class MysticBall:
    def __init__(self, strs):
        self.strs = strs

    def __call__(self, *words):
        word = choice(self.strs)
        return word

# first_ball = MysticBall(['Да', 'Нет', 'Наверное'])
first_ball = MysticBall(['Да', 'Нет', 'Наверное', 'Даже и не думай'])
for i in range(4):
    print(first_ball())
