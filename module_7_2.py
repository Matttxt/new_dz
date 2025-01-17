import pprint
def custom_write(file_name, strings):
    string_positions = {}
    read = open(file_name, 'w', encoding='utf-8')

    for i, string in enumerate(strings, 1):
        string_positions[(i, read.tell())] = string
        read.write(string + '\n')

    read.close()
    return string_positions

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]
    result = custom_write('test1.txt', info)

    pprint.pprint(result)

    f = open('test.txt', 'r', encoding='utf-8')

    print("\n")
    print(f.read())

    f.close()