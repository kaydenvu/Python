def cards():
    global total
    print("Cards values are between 2-10 or face cards.")
    cmin = 2
    cmax = 5
    face_card = ["j", "q", "k", "king", "queen", "jack", "King", "Queen", "Jack", "K", "Q", "J"]
    ace_card = ["a", "ace", "A", "Ace"]
    while True:
        c = input("Enter the number of cards you have: ")
        if c.isdigit() and cmin <= int(c) <= cmax:
            break
        else:
            print("Enter a number between 2 and 5")
    if int(c) == 2:
        m1 = input("What cards do you have? ")
        m2 = input("What cards do you have? ")
        if m1 in face_card:
            m1 = 10
        if m1 in ace_card:
            m1 = 1
        if m2 in face_card:
            m2 = 10
        if m2 in ace_card:
            m2 = 1
        if int(m2) <= 10 and int(m1) == 1:
            m1 = 11
        if int(m1) <= 10 and int(m2) == 1:
            m2 = 11
        total = int(m1) + int(m2)
    elif int(c) == 3:
        m1 = input("What cards do you have? ")
        m2 = input("What cards do you have? ")
        m3 = input("What cards do you have? ")
        if m1 in face_card:
            m1 = 10
        if m1 in ace_card:
            m1 = 1
        if m2 in face_card:
            m2 = 10
        if m2 in ace_card:
            m2 = 1
        if m3 in face_card:
            m3 = 10
        if m3 in ace_card:
            m3 = 1
        if int(m2) + int(m3) <= 10 and int(m1) == 1:
            m1 = 11
        if int(m1) + int(m3) <= 10 and int(m2) == 1:
            m2 = 11
        if int(m1) + int(m2) <= 10 and int(m3) == 1:
            m3 = 11
        total = int(m1) + int(m2) + int(m3)
    elif int(c) == 4:
        m1 = input("What cards do you have? ")
        m2 = input("What cards do you have? ")
        m3 = input("What cards do you have? ")
        m4 = input("What cards do you have? ")
        if m1 in face_card:
            m1 = 10
        if m1 in ace_card:
            m1 = 1
        if m2 in face_card:
            m2 = 10
        if m2 in ace_card:
            m2 = 1
        if m3 in face_card:
            m3 = 10
        if m3 in ace_card:
            m3 = 1
        if m4 in face_card:
            m4 = 10
        if m4 in ace_card:
            m4 = 1
        if int(m2) + int(m3) + int(m4) <= 10 and int(m1) == 1:
            m1 = 11
        if int(m1) + int(m3) + int(m4) <= 10 and int(m2) == 1:
            m2 = 11
        if int(m1) + int(m2) + int(m4) <= 10 and int(m3) == 1:
            m3 = 11
        if int(m1) + int(m2) + int(m3) <= 10 and int(m4) == 1:
            m4 = 11
        total = int(m1) + int(m2) + int(m3) + int(m4)
    elif int(c) == 5:
        m1 = input("What cards do you have? ")
        m2 = input("What cards do you have? ")
        m3 = input("What cards do you have? ")
        m4 = input("What cards do you have? ")
        m5 = input("What cards do you have? ")
        if m1 in face_card:
            m1 = 10
        if m1 in ace_card:
            m1 = 1
        if m2 in face_card:
            m2 = 10
        if m2 in ace_card:
            m2 = 1
        if m3 in face_card:
            m3 = 10
        if m3 in ace_card:
            m3 = 1
        if m4 in face_card:
            m4 = 10
        if m4 in ace_card:
            m4 = 1
        if m5 in face_card:
            m5 = 10
        if m5 in ace_card:
            m5 = 1
        if int(m2) + int(m3) + int(m4) + int(m5) <= 10 and int(m1) == 1:
            m1 = 11
        if int(m1) + int(m3) + int(m4) + int(m5) <= 10 and int(m2) == 1:
            m2 = 11
        if int(m1) + int(m2) + int(m4) + int(m5) <= 10 and int(m3) == 1:
            m3 = 11
        if int(m1) + int(m2) + int(m3) + int(m5) <= 10 and int(m4) == 1:
            m4 = 11
        if int(m1) + int(m2) + int(m3) + int(m4) <= 10 and int(m5) == 1:
            m5 = 11
        total = int(m1) + int(m2) + int(m3) + int(m4) + int(m5)
    if total == 21:
        print("Congrats! You reached Black Jack!")
    elif int(total) > 21:
        print("You went over!")
    elif int(total) < 21:
        print("Your total points were: " + str(total) + ".")


cards()
