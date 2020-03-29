import sys


def prompt_menu(menu_list, header=""):
    user_in = input(populate_menu(menu_list, header))
    if user_in == 'q':
        sys.exit(1)
    return menu_list[int(user_in) - 1]


def populate_menu(menu_list, header=""):
    output = header + "\n"

    i = 0
    for item in menu_list:
        i += 1
        output += "{}. {}\n".format(str(i), item)

    return output
