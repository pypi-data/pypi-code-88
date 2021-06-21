
def PUSH(stack,VALUE,index):
    # exception for ArrayIndexOutOfBoundary
    index += 1
    if(index < len(VALUE)):
        stack.append(VALUE[index] % 256)
    return index

def DISCARD(stack,VALUE,index):
    if(len(stack) > 0):
        stack.pop()
    return index

def ADD(stack,VALUE,index):
    # add only when there are more than two elements
    if(len(stack) >= 2):
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
    return index


def INPUT(stack,VALUE,index):
    stack.append(scrabble(input("input your own word:")))
    return index


def OUTPUT(stack,VALUE,index):
    output_ = ''
    #output only when there are at least 1 element
    if(len(stack)>0):
        output_ = chr(abs(stack.pop()%256))
    return index, output_

def SUBTRACT(stack,VALUE,index):
    # subtract only when there are more than two elements
    if(len(stack) >= 2):
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    return index


def SWAP(stack,VALUE,index):
    # swap only when there are more than two elements
    if(len(stack) >= 2):
        a = stack.pop()
        b = stack.pop()
        stack.append(a)
        stack.append(b)
    return index


def DUP(stack,VALUE,index):
    # duplicate only when there are at least 1 element
    if(len(stack) >= 1):
        a = stack.pop()
        stack.append(a)
        stack.append(a)
    return index


def SKIP_AHEAD_ZERO(stack,VALUE,index):
    a = None
    if(len(stack) != 0):
        a = stack.pop()

    index += 1
    # exception for ArrayIndexOutOfBoundary
    if(index < len(VALUE)):
        dist = VALUE[index]
    else:
        dist = 0

    if(a == 0):
        return index + dist
    else:
        return index


def SKIP_AHEAD_NONZERO(stack,VALUE,index):
    a = None
    if(len(stack) != 0):
        a = stack.pop()

    index += 1
    # exception for ArrayIndexOutOfBoundary
    if(index < len(VALUE)):
        dist = VALUE[index]
    else:
        dist = 0

    if(a != 0):
        return index + dist
    else:
        return index


def SKIP_BACK_ZERO(stack,VALUE,index):
    a = None
    if(len(stack) != 0):
        a = stack.pop()

    # exception for ArrayIndexOutOfBoundary
    if(index + 1 < len(VALUE)):
        dist = VALUE[index + 1]
    else:
        dist = 0

    if(a == 0):
        return index - dist
    else:
        return index


def SKIP_BACK_NONZERO(stack,VALUE,index):
    a = None
    if(len(stack) != 0):
        a = stack.pop()

    # exception for ArrayIndexOutOfBoundary
    if(index + 1 < len(VALUE)):
        dist = VALUE[index + 1]
    else:
        dist = 0

    if(a != 0):
        return index - dist
    else:
        return index


def STOP(stack,VALUE,index):
    return len(VALUE)


def stack(words,VALUE,debug=False):
    ACTION = {
        5: 'PUSH',
        6: 'DISCARD',
        7: 'ADD',
        8: 'INPUT',
        9: 'OUTPUT',
        10: 'SUBTRACT',
        11: 'SWAP',
        12: 'DUP',
        13: 'SKIP_AHEAD_ZERO',
        14: 'SKIP_AHEAD_NONZERO',
        15: 'SKIP_BACK_ZERO',
        16: 'SKIP_BACK_NONZERO',
        17: 'STOP',
    }

    index, index_for_print = 0, 0
    length = len(VALUE)
    stack = []
    while(index < length):
        output = ''
        n = VALUE[index]
        if(debug):
            print('{:<4} {:<18} {:>2} >> \033[1m{:<18}\033[0m'.format(index_for_print,words[index_for_print],VALUE[index_for_print],ACTION.get(n, 'NOP')),end='')

        if(n>=5 and n<= 17):
                if(n==5):
                    index = PUSH(stack,VALUE,index)
                    if(debug):
                        print('\n{:<4} {:<18} {:>2} >> {:<18}'.format(index,words[index],VALUE[index],"Value Pushed"),end='')
                if(n==6):
                    index = DISCARD(stack,VALUE,index)
                if(n==7):
                    index = ADD(stack,VALUE,index)
                if(n==8):
                    index = INPUT(stack,VALUE,index)
                if(n==9):
                    index, output = OUTPUT(stack,VALUE,index)
                if(n==10):
                    index = SUBTRACT(stack,VALUE,index)
                if(n==11):
                    index = SWAP(stack,VALUE,index)
                if(n==12):
                    index = DUP(stack,VALUE,index)
                if(n==13):
                    index = SKIP_AHEAD_ZERO(stack,VALUE,index)
                    if(index_for_print!=index-1 and debug):
                        for i in range(index_for_print+1,index+1):
                            if(i >= length):
                                break
                            print('\n{:<4} {:<18} {:>2} >> {:<18}'.format(i,words[i],VALUE[i],"Value Skipped"),end='')

                if(n==14):
                    index = SKIP_AHEAD_NONZERO(stack,VALUE,index)
                    if(index_for_print!=index-1 and debug):
                        for i in range(index_for_print+1,index+1):
                            if(i >= length):
                                break
                            print('\n{:<4} {:<18} {:>2} >> {:<18}'.format(i,words[i],VALUE[i],"Value Skipped"),end='')

                if(n==15):
                    index = SKIP_BACK_ZERO(stack,VALUE,index)
                    if(index_for_print!=index and debug):
                        for i in reversed(range(index,index_for_print)):
                            if(i < 0):
                                break
                            print('\n{:<4} {:<18} {:>2} >> {:<18}'.format(i,words[i],VALUE[i],"Value Skipped"),end='')

                if(n==16):
                    index = SKIP_BACK_NONZERO(stack,VALUE,index)
                    if(index_for_print!=index and debug):
                        for i in reversed(range(index,index_for_print)):
                            if(i < 0):
                                break
                            print('\n{:<4} {:<18} {:>2} >> {:<18}'.format(i,words[i],VALUE[i],"Value Skipped"),end='')

                if(n==17):
                    index = STOP(stack,VALUE,index)
                #moving to next index
                index += 1
        else:
            #non
            index += 1

        # debug

        # update index_for_print
        index_for_print = index

        if(debug):
            print(" >> ",stack)

        # check if we have an output (9), then print it
        if output != '' and debug:
            print("\033[1moutput: \033[0m" + output + "\n")
        else:
            print(output, end='')
    print()


def beatnik_run(text,debug=False):
    word = beatnik.preprocess(text)
    VALUE = []
    for i in word:
        value = beatnik.scrabble(i)
        VALUE.append(value)
    beatnik.stack(word,VALUE,debug=debug)
