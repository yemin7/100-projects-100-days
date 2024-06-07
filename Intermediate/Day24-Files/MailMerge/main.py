letter = open("starting_letter.txt", "r")
content = letter.read()
letter.close()

with open("invited_names.txt") as file:
    names = file.readlines()
    for i in names:
        name = i.strip()
        with open(f"./Invite_Letters/invited_{name}.txt", "w") as invite:
            new_letter = content.replace("[name]", name)
            invite.write(new_letter)
