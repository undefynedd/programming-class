name = input('who the FUCK are you????')
yes = " " * (len(name)//2)

no = False

for char in name:
    yes += char
    print(yes)
    no = not no
    if no:
        yes = yes[1:]
