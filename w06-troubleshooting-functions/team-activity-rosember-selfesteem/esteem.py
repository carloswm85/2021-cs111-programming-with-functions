def main():
    print('This program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten statements that you could possibly apply to yourself. Please rate how much you agree with each of the statements by responding with one of these four letters:')
    print('D means you strongly disagree with the statement.')
    print('d means you disagree with the statement.')
    print('a means you agree with the statement.')
    print('A means you strongly agree with the statement.')

    options = [
        ['I feel that I am a person of worth, at least on an equal plane with others.', 1],
        ['I feel that I have a number of good qualities.', 1],
        ['All in all, I am inclined to feel that I am a failure.', 0],
        ['I am able to do things as well as most other people.', 1],
        ['I feel I do not have much to be proud of.', 0],
        ['I take a positive attitude toward myself.', 1],
        ['On the whole, I am satisfied with myself.', 1],
        ['I wish I could have more respect for myself.', 0],
        ['I certainly feel useless at times.', 0],
        ['At times I think I am no good at all.', 0]]

    final_score = 0
    for option in options:
        print('For the next statement: ')
        print(f'"{option}"')
        selection = input('Enter an option D, d, a, or A: ')
        feeling_value = option[1]
        value = func(selection, feeling_value)
        final_score = final_score + value

    print(f'Your score is {final_score}.')
    print('A score below 15 may indicate problematic low self-esteem')


def func(sel, fv):
    if fv == 1 and sel == 'A':
        return 3
    if fv == 1 and sel == 'a':
        return 2
    elif fv == 1 and sel == 'd':
        return 1
    elif fv == 1 and sel == 'D':
        return 0
    elif fv == 0 and sel == 'A':
        return 0
    elif fv == 0 and sel == 'a':
        return 1
    elif fv == 0 and sel == 'd':
        return 2
    elif fv == 0 and sel == 'D':
        return 3
    else:
        return -1


if __name__ == "__main__":
    main()
