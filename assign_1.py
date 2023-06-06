import csv


def count_words(text: str) -> int:
    return len(text.split())


def count_words_with_condition(text: str, condition_func) -> int:
    counter = 0
    for word in text.split():
        if condition_func(word):
            counter += 1
    return counter


def is_titlecase(word: str) -> bool:
    return len(word) > 0 and word[0].isupper()


def is_capitalized(word: str) -> bool:
    return len(word) > 0 and word.isupper() and not word[0].isdigit()


def is_lowercase(word: str) -> bool:
    return word.islower()


def is_numeric(word: str) -> bool:
    return word.isnumeric()


def sum_numbers(text: str) -> int:
    total = 0
    for word in text.split():
        if word.isnumeric():
            total += int(word)
    return total


def generate_graphical_output(text: str):
    graph_dict = {}
    for word in text.split():
        length = sum(1 for char in word if char.isalnum())
        graph_dict[length] = graph_dict.get(length, 0) + 1
    sorted_dict = dict(sorted(graph_dict.items()))

    for length, count in sorted_dict.items():
        print(f"{length:>3}|{'*' * count:18}|{count:>2}")


if __name__ == "__main__":


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


def login(logins):
    username_input = input("Please provide your username: ")
    if username_input not in logins:
        quit("Unregistered user, exit program")

    userpass_input = input("Please provide your password: ")
    if userpass_input != logins[username_input]:
        quit("Incorrect password, exit program")

    print("----------------------------------------")
    print(f"Welcome to the app, {username_input}")
    print("We have 3 texts to be analyzed")
    print("----------------------------------------")
    return int(input("Enter a number between 1 and 3 to select a text: ")) - 1


def analyze_text(text_index):
    if not 0 <= text_index < len(TEXTS):
        quit("The provided number is not correct. You must choose 1, 2, or 3")

    selected_text = TEXTS[text_index]
    print("----------------------------------------")
    print(f"There are {count_words(selected_text)} words in the selected text.")
    print(f"There are {count_words_with_condition(selected_text, is_titlecase)} titlecase words.")
    print(f"There are {count_words_with_condition(selected_text, is_capitalized)} uppercase words.")
    print(f"There are {count_words_with_condition(selected_text, is_lowercase)} lowercase words.")
    print(f"There are {count_words_with_condition(selected_text, is_numeric)} number strings.")
    print(f"The sum of all the numbers: {sum_numbers(selected_text)}")
    print("----------------------------------------")
    print("LEN|    OCCURRENCES    |NR.")
    print("----------------------------------------")
    generate_graphical_output(selected_text)


def main():
    with open("user_logins.csv") as logins_file:
        next(logins_file)
        logins = dict(row for row in csv.reader(logins_file, delimiter=","))

    text_index = login(logins)
    analyze_text(text_index)

    print("Program finished successfully!")



