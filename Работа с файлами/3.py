import os
def find_directories_with_py_files(root_dir):
    py_directories = set()

    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                py_directories.add(root)

    return sorted(py_directories)


root_directory = '.'

py_directories = find_directories_with_py_files(root_directory)

with open('akdjlaksjd.txt', 'w') as result_file:
    for directory in py_directories:
        result_file.write(directory + '\n')