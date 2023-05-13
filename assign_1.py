import csv


def word_count(text: str) -> int:
    counter = 0
    for word in text.split(sep=" "):
        counter += 1
    return counter


def titlecase_count(text: str) -> int:
    counter = 0
    for word in text.split(sep=" "):
        if len(word) > 0 and word[0].isupper():
            counter += 1
    return counter


def capitalize_count(text: str) -> int:
    counter = 0
    for word in text.split(sep=" "):
        if len(word) > 0 and word.isupper() and not word[0].isdigit():
            counter += 1
    return counter


def lowercase_count(text: str) -> int:
    counter = 0
    for word in text.split(sep=" "):
        if word.islower():
            counter += 1
    return counter


def numbers_count(text: str) -> int:
    counter = 0
    for word in text.split(sep=" "):
        if word.isnumeric():
            counter += 1
    return counter


def numbers_sum(text: str) -> int:
    counter = 0
    for word in text.split(sep=" "):
        if word.isnumeric():
            counter += int(word)
    return counter


def graphical_output(text: str):
    graph_list = []
    for word in text.split():
        count = int(len(word))
        graph_list.append(count)
    graph_dict = {}
    for num in graph_list:
        if num in graph_dict:
            graph_dict[num] += 1
        else:
            graph_dict[num] = 1
    sorted_dict = dict(sorted(graph_dict.items()))
    # max_length_word = max(graph_list)
    # for count in sorted_dict:
    #     asterisks = "*" * count[1]
    #     spaces = " " * (max_length_word - count[1])
    #     bar = asterisks + spaces
    #     print(f"{str(count[0]).rjust(2)} |{bar} | {str(count[1]).rjust(1)}")
    for length, count in sorted_dict.items():
        print(f"{length:>3}|{'*' * count:18}|{count:>2}")



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


with open("user_logins.csv") as logins_file:
    next(logins_file)
    logins = dict([row for row in csv.reader(logins_file, delimiter=",")])

# print(logins)

username_input = input("Please provide your username: ")

logged = False
if username_input in logins:
    userpass_input = input("Please provide your password: ")
    if userpass_input == logins[username_input]:
        logged = True
    else:
        quit("Incorrect password, exit program")
else:
    quit("Unregistered user, exit program")

if logged:
    print("----------------------------------------")
    print(f"Welcome to the app, {username_input}")
    print("We have 3 texts to be analyzed")
    print("----------------------------------------")
    selected_text = input("Enter a number btw. 1 and 3 to select: ")
    if selected_text not in ["1", "2", "3"]:
        quit("provided number is not correct, you must choose 1, 2 or 3")
    selected_text = int(selected_text)
    chosen_number = selected_text - 1
    print("----------------------------------------")
    print(f"There are {word_count(TEXTS[chosen_number])} words in the selected text.")
    print(f"There are {titlecase_count(TEXTS[chosen_number])} titlecase words.")
    print(f"There are {capitalize_count(TEXTS[chosen_number])} uppercase words.")
    print(f"There are {lowercase_count(TEXTS[chosen_number])} lowercase words.")
    print(f"There are {numbers_count(TEXTS[chosen_number])} number string.")
    print(f"The sum of all the numbers {numbers_sum(TEXTS[chosen_number])}")
    print("----------------------------------------")
    print("LEN|    OCCURENCES    |NR.")
    print("----------------------------------------")
    print(graphical_output(TEXTS[chosen_number]))

quit("Program finished successfully!")
