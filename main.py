from bottle import route, run

@route('/hello')
def hello():
    return "Hello World!"


from ensurepip import version


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('HEY GUYS ITS WURKINNN')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
