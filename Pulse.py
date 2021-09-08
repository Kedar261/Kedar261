pulse = int(input("2. Type your Pulse Rate"))
def pulsecheck():
    if pulse in range(72,101):
        print("The Pulse is normal")
    else:
        print("The Pulse is not normal")
pulsecheck()
