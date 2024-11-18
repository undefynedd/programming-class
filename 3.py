name = input('who the FUCK are you????')
yes = " " * (len(name)//2)
if len(name)%2 == 1:
    name = name + "."

no = False

for char in name:
    yes += char
    if no:
        print(yes)
        yes = yes[1:]
    no = not no
