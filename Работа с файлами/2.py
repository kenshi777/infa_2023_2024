def write_array(array, file_name):
    """записывает строки из array в файл file_name"""
    with open(file_name, 'w') as file:
        file.writelines(array)

write_array(['sosiski\n', 'pechenki\n', 'chipsiki\n'], 'lox.txt')
