"""Алла ошиблась при копировании из одной структуры данных в другую. Она хранила массив чисел в кольцевом буфере.
Массив был отсортирован по возрастанию, и в нём можно было найти элемент за логарифмическое время. Алла скопировала
данные из кольцевого буфера в обычный массив, но сдвинула данные исходной отсортированной последовательности. Теперь
массив не является отсортированным. Тем не менее, нужно обеспечить возможность находить в нем элемент за O ( log n )
. Можно предполагать, что в массиве только уникальные элементы.
 """


def broken_search(nums, target) -> int:
    def search(left, right):
        mid = (left + right) // 2
        if left == right:
            return -1
        mid_value = nums[mid]
        if mid_value == target:
            return mid
        if (mid_value < nums[left] <= target
                or nums[left] <= target < mid_value
                or target < mid_value < nums[left]):
            return search(left, mid)
        else:
            return search(mid + 1, right)

    return search(0, len(nums))


if __name__ == '__main__':
    print(broken_search(list(map(int, input().split())), int(input())))
