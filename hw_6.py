# #[a-f0-9]+ colors
# ^(?:[A-Za-z]+[-\']?[A-Za-z]?[A-za-z]+\s)+ names and surnames
# \s[A-Za-z]+\.[a-z0-9]+ file names
# \s[A-Za-z0-9]+\@[a-z0-9]+[\.{2}a-z-]+ emails

import re

while True:
    with open('MOCK_DATA.txt', 'r') as file:
        content = file.read()
    search_input = int(input('Names - 1, Colors - 2, files - 3, emails - 4, exit - 5'))
    if search_input == 1:

        names_list = re.findall(r'^(?:[A-Za-z]+[-\']?[A-Za-z]?[A-za-z]+\s+)', content)
        print(names_list)
        with open('names.txt', 'w') as file_1:
            for name in names_list:
                file_1.write(f'{name}\n')
    elif search_input == 2:
        colors_list = re.findall(r'#[a-f0-9]+ colors', content)
        with open('colors.txt', 'w') as file_2:
            for color in colors_list:
                file_1.write(f'{color}\n')

    elif search_input == 3:
        files_list = re.findall(r'(?:\s[?:A-Za-z]+\.[a-z0-9]+])+', content)
        with open('files.txt', 'w') as file_3:
            for file in files_list:
                file_1.write(f'{file}\n')

    elif search_input == 4:
        emails_list = re.findall(r'\s[A-Za-z0-9]+\@[a-z0-9]+[\.{2}a-z-]+', content)
        with open('files.txt', 'w') as file_3:
            for email in emails_list:
                file_1.write(f'{email}\n')
    elif search_input == 5:
        break

    else:
        print("don't print other numbers except 1, 2, 3, 4, 5")
