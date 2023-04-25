try:
    with open("with.txt", "r") as f:
        string = f.read()
    for word in string.splitlines():
        if 'am' in word:
            print(word)
except Exception as e:
    print(e)
    print("Error: " + str(e))
