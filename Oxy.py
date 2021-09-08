oxycheck = int(input("3. Type your Oxygen rate"))
def oxygenlevel():
    if oxycheck in range(88,101):
        print("The Oxygen level is normal")
    else:
        print("The Oxygen Level is not normal")
oxygenlevel()
