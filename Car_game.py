is_started = False
while True:
    cmd = input("Command > ").upper()
    if cmd == "START" and not is_started:
        print("Car Started")
    elif cmd == "STOP" and is_started:
        print("Car Stopped")
    elif cmd == "HELP":
        print('''
        1. START
        2. STOP
        3. QUIT
        ''')
    elif cmd == "QUIT":
        break

print("Bye")


