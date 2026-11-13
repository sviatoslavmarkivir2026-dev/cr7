def find_unique(numbers):
    basket = set()
    for number in numbers:
        if -number in basket:
            basket.remove(-number)
        else:
            basket.add(number)
    return basket


test_list = [int(x) for x in input('Введіть послідовність: ').split()]
print(find_unique(test_list))