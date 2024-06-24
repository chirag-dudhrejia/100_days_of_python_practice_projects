import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetics():
    name = input("Enter string here to get Nato codes : ").upper()
    try:
        result_dict = {letter: phonetic_dict[letter] for letter in name}
    except KeyError:
        print("Sorry, only letters allowed.")
        generate_phonetics()
    else:
        for letter, code in result_dict.items():
            print(f"{letter} : {code}")


generate_phonetics()
