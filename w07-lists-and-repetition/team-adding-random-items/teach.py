import random


def main():
    randnums = [16.2, 75.1, 52.3]
    print(randnums)
    append_random_numbers(randnums)
    print(randnums)
    append_random_numbers(randnums, 3)
    print(randnums)
    randwords = []
    append_random_words(randwords, 4)
    print(randwords)


def append_random_numbers(numbers_list, quantity=1):
    for i in range(quantity):
        rand_num = random.uniform(0, 100)
        round_num = round(rand_num, 1)
        numbers_list.append(round_num)


def append_random_words(words_list, quantity=1):
    new_list = ["Argentina", "Nigeria", "United States", "Mexico", "Guatemala"]
    length = len(new_list)
    index = random.randrange(length)
    words_list.append(new_list[index])


if __name__ == "__main__":
    main()
