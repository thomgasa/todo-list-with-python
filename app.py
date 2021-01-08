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
    

def print_list():
    """ Doc-string
    esta función imprime en consola las tareas guardadas
    en la variable todos
    """
    global todos
    i=0
    for index in todos:
        i=i+1
        print(f'{i}-. {index}')
    
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
    en el cual agrega las tareas delimitadas por línea nueva
    """
    # your code here
    with open('todos.csv', 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter='\n')
        writer.writerow(todos)
    
def load_todos():
    # your code here
    """ Doc-string
    esta función carga el archivo .csv
    luego limpia la variable todos en ejecución y agrega los valores
    del .csv a la variable en ejecución, finalmente imprime la lista en 
    consola pero esta vez delimitada por líneas nuevas.
    Esta es la función que debería usar el usuario común, 
    dónde además verifica que el archivo .csv está correcto
    """
    with open('todos.csv', newline='\n') as csvfile:
        reader=csv.reader(csvfile)
        list.clear(todos)
        i=1
        for row in reader:
            i=i+1
            print(f'\n {i}'.join(row))
            todos.append(*row) #el * rompe la lista y muestra elementos
    

# Below this code will only run if the entry file running was app.py
""""importante  la línea donde el código es:
        if __name__ == '__main__':
    El nombre del módulo principal siempre será main, en este caso
    para ejecutar este archivo se ejecuta el módulo app.py
    y cómo todo el código se encuentra en este módulo entonces
    el __name__ predeterminado del módulo será: __main__

    En caso contrario, si el código se encontrara en un archivo llamado
    code.py, y ese módulo se importa al módulo app.py y el archivo que 
    se ejecuta es app.py, entonces el __name__ predeterminado del módulo 
    code.py sería: code

    por lo que la línea de código debería cambiar a:
        if __name__ == 'code':
"""
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