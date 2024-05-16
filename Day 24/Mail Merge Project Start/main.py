# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", "r") as file:
    raw_names = file.readlines()

names = [sub.replace('\n', '') for sub in raw_names]

with open("./Input/Letters/starting_letter.txt", "r") as file:
    invitation_blueprint = file.read()


for name in names:
    invitation = invitation_blueprint.replace("[name]", name)
    with open(f"./Output/ReadyToSend/invitation for {name}.txt", "w") as file:
        file.write(str(invitation))
