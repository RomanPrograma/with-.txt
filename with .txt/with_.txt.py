
try:
    with open( "with_.txt", "r" ) as f:
        content = f.readlines()
        n = int(input("Enter quantity lines: "))

        for num, line in enumerate(content[-n:]):
            print( line, end='')
        print()
        if n > len(content):
            print( "Error: The file does not have that many lines", end= '' )
        elif n < len(content):
            print()
except Exception as e:
    print( "Error: " + str(e) )
finally:
    f.close()