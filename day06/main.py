def read_input():
    return [ int(n) for n in input().split(',')]

def answer_1(initial_state):
    #print("Initial State: {}".format(initial_state))
    for i in range(80):
        length = len(initial_state)
        for n in range(length):
            if initial_state[n] == 0:
                initial_state[n] = 7
                initial_state.append(8)
            initial_state[n] -= 1
        #print("After  {} day: {}".format(i+1, initial_state))
    return len(initial_state)

def answer_2(initial_state):
    #print("Initial State: {}".format(initial_state))
    buckets = [0, ]*9
    for n in initial_state:
        buckets[n] += 1

    for i in range(256):
        parent = buckets.pop(0)
        buckets[6] += parent
        buckets.append(parent)
    return sum(buckets)
if __name__ == '__main__':
    initial_state = read_input()

    #print(answer_1(initial_state))
    print(answer_2(initial_state))
