"""Задание связано с обратной польской нотацией. Она используется для парсинга арифметических выражений. Еще её
иногда называют постфиксной нотацией.

В постфиксной нотации операнды расположены перед знаками операций.

Пример 1:
3 4 +
означает 3 + 4 и равно 7

Пример 2:
12 5 /
Так как деление целочисленное, то в результате получим 2.

Пример 3:
10 2 4 * -
означает 10 - 2 * 4 и равно 2"""

OPERATORS = {
    '+': lambda left, right: left + right,
    '-': lambda left, right: left - right,
    '*': lambda left, right: left * right,
    '/': lambda left, right: left // right,
}
ERROR_EMPTY_STACK = 'Empty stack'
ERROR_DIGITIZATION = 'Digitization is failed: {element}'


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError(ERROR_EMPTY_STACK)


def calculator(expression, stack=None, operators=OPERATORS, digitizer=int):
    stack = Stack() if stack is None else stack
    for element in expression:
        if element in operators:
            right, left = stack.pop(), stack.pop()
            stack.push(operators[element](left, right))
        else:
            try:
                stack.push(digitizer(element))
            except ValueError:
                raise ValueError(ERROR_DIGITIZATION.format(element=element))
    return stack.pop()


if __name__ == '__main__':
    print(calculator(input().split(' ')))
