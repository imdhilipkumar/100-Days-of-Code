PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_list:
    names = name_list.readlines()
    print(names)
with open("./Input/Letters/starting_letter.txt") as letter_list:
    letters = letter_list.read()
    print(letters)
    for name in names:
        stripped_name = name.strip()
        new_letters = letters.replace(PLACEHOLDER, stripped_name)
        print(new_letters)
        with open(f"./Output/ReadyToSend/letter for {stripped_name}.txt", mode="w") as final_letter:
            final_letter.write(new_letters)
