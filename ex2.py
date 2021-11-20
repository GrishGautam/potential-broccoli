final = ""
n=0
o=0
while final != "QUIT":

    inp = input("write about the car else type help > ")
    final = inp.upper()

    if final == "HELP":
        print("type start to start the car")
        print("type stop to stop the car")
        print("type quit to quit the car")

    elif final == "START":
        n = n + 1
        if n < 2:
            print("ready to go....the car is driving")
        else:
            print("the car has started")

    elif final == "STOP":
        o =+ 1
        if o < 2 and n > 1:
            print("the car stopped")
        elif o < 2 and n != 0:
            print("car hasent started yet")
        else:
            print("the car has already stopped")
    else:
        print("computer doesnot understands this of word")
