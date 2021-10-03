"""Гоша реализовал структуру данных Дек, максимальный размер которого определяется заданным числом. Методы push_back(
x), push_front(x), pop_back(), pop_front() работали корректно. Но, если в деке было много элементов,
программа работала очень долго. Дело в том, что не все операции выполнялись за O(1). Помогите Гоше! Напишите
эффективную реализацию.

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 5000. Во второй строке
записано число m — максимальный размер дека. Он не превосходит 1000. В следующих n строках записана одна из команд:
push_back(value) – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов,
вывести «error». push_front(value) – добавить элемент в начало дека. Если в деке уже находится максимальное число
элементов, вывести «error». pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести
«error». pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error». Value —
целое число, по модулю не превосходящее 1000.

Формат вывода
Выведите результат выполнения каждой команды на отдельной строке. Для успешных запросов push_back(x) и
push_front(x) ничего выводить не надо."""

ERROR = 'error'
COMMAND_ERROR = 'Error in command:{command}'


class Deque:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size
        self.head = 1
        self.tail = 0
        self.size = 0

    def push_front(self, value):
        if self.size == self.max_size:
            raise RuntimeError(ERROR)
        self.head = (self.head - 1) % self.max_size
        self.items[self.head] = value
        self.size += 1

    def push_back(self, value):
        if self.size == self.max_size:
            raise RuntimeError(ERROR)
        self.tail = (self.tail + 1) % self.max_size
        self.items[self.tail] = value
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            raise RuntimeError(ERROR)
        value = self.items[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return value

    def pop_back(self):
        if self.size == 0:
            raise RuntimeError(ERROR)
        value = self.items[self.tail]
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return value


if __name__ == '__main__':
    command_count = int(input())
    deque = Deque(max_size=int(input()))
    for _ in range(command_count):
        try:
            command, *params = input().split(' ')
            result = getattr(deque, command)(*params)
            if 'pop' in command:
                print(result)
        except RuntimeError:
            print(ERROR)
        except AttributeError:
            raise ValueError(COMMAND_ERROR.format(command=command))
