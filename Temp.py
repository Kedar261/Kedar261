temp = int(input("4. Type your Body temp in FH"))
def tempcheck():
    if temp in range(97,101):
        print("The Temperature is normal")
    else:
        print("The Temperature is not normal")

