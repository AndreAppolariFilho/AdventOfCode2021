def read_input():
    return [ int(n) for n in input().split(',')]

def answer_01(numbers):
    min_cost = 9999999999999
    for i in range(min(numbers), max(numbers)):
        min_cost = min(sum([abs(number - i) for number in numbers]), min_cost)
    return min_cost

def pa(number):
    return ((1 + number) * number)/2

def answer_02(numbers):
    min_cost = 9999999999999
    for i in range(min(numbers), max(numbers)):
        min_cost = min(sum([pa(abs(number - i)) for number in numbers]), min_cost)
    return min_cost
if __name__ == '__main__':
    numbers = read_input()
    print(answer_01(numbers))
    print(answer_02(numbers))
