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
означает 10 - 2 * 4 и равно 2

Разберём последний пример подробнее:

Знак * стоит сразу после чисел 2 и 4, значит к ним нужно применить операцию, которую этот знак обозначает,
то есть перемножить эти два числа. В результате получим 8.

После этого выражение приобретёт вид:

10 8 -

Операцию «минус» нужно применить к двум идущим перед ней числам, то есть 10 и 8. В итоге получаем 2.

Рассмотрим алгоритм более подробно. Для его реализации будем использовать стек.

Для вычисления значения выражения, записанного в обратной польской нотации, нужно считывать выражение слева направо и
придерживаться следующих шагов:

Обработка входного символа: Если на вход подан операнд, он помещается на вершину стека. Если на вход подан знак
операции, то эта операция выполняется над требуемым количеством значений, взятых из стека в порядке добавления.
Результат выполненной операции помещается на вершину стека. Если входной набор символов обработан не полностью,
перейти к шагу 1. После полной обработки входного набора символов результат вычисления выражения находится в вершине
стека. Если в стеке осталось несколько чисел, то надо вывести только верхний элемент. """

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
