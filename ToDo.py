print ('''Hi! It's my ToDo''')
todos = []
first = input('Enter first case:  ')
todos.append (first)
menu =  '1. Add \n' \
        '2. Change \n' \
        '3. Delete \n' \
        '4. Print \n' \
        '0. Exit'


def add_todo():
    add = input ("")
    todos.append (add)

def change_todo():
    change_num= int (input('Enter change number: '))
    change_txt = input ('Enter new case: ')
    todos [change_num - 1] = change_txt
    
def delete_todo():
	del_num = int (input('Enter del number: '))
	todos.pop(del_num - 1)
	
def print_todos():
	print(*todos, sep ='\n')
	
	
while True:
    print (menu)
    command = input ('')
    if command not in ['1', '2', '3', '4', '0']:
        print ('Error')
        continue
    if command == '1':
        add_todo ()
        continue
    elif command == '2':
        change_todo()
        continue
    elif command == '3':
        delete_todo()
        continue
    elif command == '4':
        print_todos()
        continue
    elif command == '0':
        exit
        break

