import csv

todos = []
stop = False

def get_todos():
    global todos
    return todos

def add_one_task(title):
    # your code here
    """ Doc-string
    esta función agrega el título de la tarea escrita
    por el usuario y la agrega a la variable todos
    """
    todos.append(title)
    print(todos)
    pass

def print_list():
    """ Doc-string
    esta función imprime en consola las tareas guardadas
    en la variable todos, sólo debería usarse como control
    """
    global todos
    print(todos)
    
def delete_task(number_to_delete):
    """ Doc-string
    esta función elimina la tarea posicionada en el lugar
    que el usuario elija
    """
    # your code here
    todos.pop(int(number_to_delete)-1)

def save_todos():
    """ Doc-string
    esta función crea/escribe un documento todos.csv
    en el cual agrega las tareas delimitadas por ,
    """
    # your code here
    with open('todos.csv', 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(todos)
    
def load_todos():
    # your code here
    """ Doc-string
    esta función carga la lista de tareas en el .csv
    luego limpia la variable (todos) y agrega en los valores
    de la lista todos, finalmente imprime la lista en 
    consola pero esta vez delimitada por líneas nuevas.
    Esta es la función que debería usar el usuario común, 
    dónde además verifica que el archivo .csv está correcto
    """
    with open('todos.csv', newline='\n') as csvfile:
        reader=csv.reader(csvfile)
        list.clear(todos)
        for row in reader:
            print('\n'.join(row))
            todos.append(row)
    

# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")