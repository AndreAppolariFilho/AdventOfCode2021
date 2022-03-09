def read_input():
    list_commands = []
    try:
        while True:
            list_commands.append(input().strip())
    except Exception as e:
        print(e)
    return list_commands

def print_message(character, found):
    if character == '[':
        print('Expected ] but found a '+found)
    if character == '{':
        print('Expected } but found a '+found)
    if character == '(':
        print('Expected ) but found a ' + found)
    if character == '<':
        print('Expected < but found a ' + found)

def evalute_command(command):
    stack = []
    illegal_mapping = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    illegal_counting = {
        ')': 0,
        ']': 0,
        '}': 0,
        '>': 0
    }
    for character in command:
        if character == '{' or character == '(' or character == '[' or character == '<':
            stack.append(character)
        if character == '}':
            compare = stack.pop()
            if compare != '{':
                illegal_counting[character] += 1
                print_message(compare, character)
                break
        if character == ')':
            compare = stack.pop()
            if compare != '(':
                illegal_counting[character] += 1
                print_message(compare, character)
                break
        if character == ']':
            compare = stack.pop()
            if compare != '[':
                illegal_counting[character] += 1
                print_message(compare, character)
                break
        if character == '>':
            compare = stack.pop()
            if compare != '<':
                illegal_counting[character] += 1
                print_message(compare, character)
                break

    return sum([illegal_counting[key] * illegal_mapping[key] for key in illegal_counting])

def autocomplete(command):
    stack = []
    has_error = False
    illegal_mapping = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }
    for character in command:
        if character == '{' or character == '(' or character == '[' or character == '<':
            stack.append(character)
        if character == '}':
            compare = stack.pop()
            if compare != '{':
                has_error = True
                break
        if character == ')':
            compare = stack.pop()
            if compare != '(':
                has_error = True
                break
        if character == ']':
            compare = stack.pop()
            if compare != '[':
                has_error = True
                break
        if character == '>':
            compare = stack.pop()
            if compare != '<':
                has_error = True
                break
    if not has_error:
        total_score = 0

        for word in reversed(stack):
            multiply = 5 * total_score
            total_score = multiply + illegal_mapping[word]

        return total_score

    return 0


def answer_01(list_of_commands):
    return sum([evalute_command(command) for command in list_of_commands])

def answer_02(list_of_commands):
    result = sorted([ autocomplete(command) for command in list_of_commands])
    result = [number for number in result if number != 0]
    return result[len(result)//2]

if __name__ == '__main__':
    list_of_commands = read_input()
    print(answer_01(list_of_commands))
    print(answer_02(list_of_commands))