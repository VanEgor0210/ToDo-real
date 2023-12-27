class Todo:
    menu = {'1': 'Добавить новое дело', '2': 'Открыть мой список дел', '3': 'Найти моё дело', '4': 'Расказать о готовности моего дела'}
 
    def __init__(self):
        self.todo_items = []  # Список дел
 
    def add_todo(self, items):
        self.todo_items.append(items)
 
    def list(self):
        print('Список дел:')
        for item in self.todo_items:
            print(str(item.num) + '. ' + item.todo + ' (Выполнено)' * int(item.is_done))
        print()
 
    def find(self, find_str):
        return ((item.num, item.todo) for item in self.todo_items if item.todo.find(find_str) != -1)
 
    def run(self):
 
        while True:
            print('Меню:     (Функции работают по их цифре)')
            for num, val in Todo.menu.items():
                print(num + '. ' + val, end='\n')
            command = input()
            if command == '1':
                self.add_todo(TodoItem(input('Какое дело? ')))
                print('Новое дело добавлено в мой список')
            elif command == '2':
                self.list()
            elif command == '3':
                find = self.find(input('Введите главное слово? '))
                for num, val in find:
                    print(str(num) + '. ' + val)
            elif command == '4':
                num = int(input('Введите номер дела для обозначения его выполнения: '))
                for item in self.todo_items:
                    if item.num == num:
                        item.check()
                        print(f'Дело под номером {num} теперь обозначено как выполненое')
                        break
                else:
                    print(f'Дело {num} не найдено в твоём списке ')

 
 
class TodoItem:
    couner_do = 0
 
    def __init__(self, new_do):
        self.is_done = False
        TodoItem.couner_do += 1
        self.num = TodoItem.couner_do
        self.todo = new_do
 
    def check(self):
        self.is_done = True
 
    def uncheck(self):
        self.is_done = False
 
 
if __name__ == '__main__':
    todo_1 = Todo()
    todo_1.run()
