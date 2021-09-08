bp = int(input("1. Type your Blood pressure"))
def bloodpressuresystolic():
    if bp in range(120,141):
        print("The BP is normal")
    else:
        print("The BP is not normal")
bloodpressuresystolic()
