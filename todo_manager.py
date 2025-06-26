import json
import os

TODO_FILE = "todo.json"

def load_todos():
    """Load todos from file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    """Save todos to file."""
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=2)

def main():
    todos = load_todos()
    
    while True:
        print("\nTodo List Manager")
         print("1. Add Todo")
          print("2. List Todos")
           print("3. Delete Todo")
            print("4. Exit")
        
            choice = input("Choose an option: ")
        
              if choice == "1":
            todo = input("Enter todo: ")
          todos.append({"task": todo, "done": False})
       save_todos(todos)
    print("Todo added!")
        
 elif choice == "2" 
    for i, todo in enumerate(todos, 1):
        status = "✓" if todo["done"] else " "
            print(f"{i}. [{status}] {todo['task']}")
        
                elif choice == "3":
                  index = int(input("Enter todo number to delete: ")) - 1
                      if 0 <= index < len(todos):
                       todos.pop(index)
                         save_todos(todos)
                           print("Todo deleted!")
            else:
                print("Invalid number.")
        
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
