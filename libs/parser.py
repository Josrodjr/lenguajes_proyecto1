# define the rules of the program

# separador = ' '

operandos = {
    ' ': 1,
    '|': 1,
    '*': 2,
    '+': 2,
    '?': 1
}

def parse_input(text):
    # parsed input result
    parsed = []
    # parenthesis closure counters
    parenthesis_cont = 0
    # current token detected
    token = ''
    # for loop for recieved text
    for char in range(len(text)):
        if text[char] == '(' or text[char] == ')':
            if parenthesis_cont >= 1:
                token += text[char]
        if text[char] == '(':
            parenthesis_cont += 1
        if text[char] == ')':
            # TODO: send the current token found to same function in recursive motive
            if parenthesis_cont == 1:
                result = parse_input(token)
                parsed.append(result)
                token = ''
            # TODO: empty found token
            parenthesis_cont -= 1
        # if text[char] == ' ':
        #     # append to parsed the current value
        #     if token != '':
        #         parsed.append(token)
        #     # empty found char
        #     token = ''
        if text[char] in operandos and parenthesis_cont == 0:
            if token != '':
                parsed.append(token)
            token = ''
            token += text[char]
            parsed.append(token)
            token = ''
        # if none of the above do a concat to current found token and keep looking
        elif text[char] != '(' and text[char] != ')':
            token += text[char]
        if char == len(text)-1:
            parsed.append(token)
    return parsed


# test_clause2 = '(a|b)* palabra palabra palabra'
# test_clause = '(palabra (letra|letra)* a a b)* a'
# a = parse_input(test_clause)
# print(a)