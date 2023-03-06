# Написать декоратор call_times, который будет принимать в качестве параметра file_name,
# считать количество вызовов функций и записывать в файл в формате f'{func_name} была вызвана {count} раза.\n'


counter = {}
text = 'Function {} was called {} times.\n'
lines = []

def call_times(file_name):
    def inner(func):
        def wrapper():
            prev_counter = counter[func.__name__] if func.__name__ in counter else 0
            next_counter = prev_counter + 1
            counter[func.__name__] = next_counter
            if prev_counter:
                prev_line = text.format(func.__name__, prev_counter)
                with open(file_name, 'r') as f:
                    for line in f.readlines():
                        if line == prev_line:
                            line == text.format(func.__name__, next_counter)
                        lines.append(line)
                with open(file_name, 'a') as f:
                    f.write(text.format(func.__name__, next_counter))

        return wrapper

    return inner


@call_times('deco_test.txt')
def baa():
    pass


@call_times('deco_test.txt')
def daa():
    pass


@call_times('deco_test.txt')
def zaa():
    pass


for i in range(5):
    baa()

for i in range(7):
    daa()

for i in range(4):
    zaa()

print(counter)
print(lines)
lines.clear()