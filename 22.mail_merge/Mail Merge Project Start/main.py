#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    temp_names_list = file.readlines()
names_list = []

for name in temp_names_list:
    names_list.append(name.rstrip('\n'))

with open(
        "Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    example = file.read()

for name in names_list:
    letter = example.replace("[name]", f"{name}")
    with open(f"Mail Merge Project Start/Input/Letters/{name}.txt",
              mode="w") as file:
        file.write(letter)
