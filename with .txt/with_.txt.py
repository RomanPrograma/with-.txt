


try:
    with open("with.txt", "r") as f:
        content = f.read().splitlines()
        n = int(input("delete a line by its number in the file or by content\nif by nomber choose - 1\nif by content chose - 2\n"))
        if n < 1 :
           raise ValueError('please enter a number greater than 0')
        elif n > 2:
            raise ValueError('please enter a number less than 3')
        elif n == 1:
            m = input("Enter  the content of the line to be deleted: ")
            deleted_str_1 = content.remove(m)
            print(content)
        elif n == 2:
            x = int(input("Enter the line number to be deleted: "))
            if x > len(content):
                print( "Error: The file does not have that many lines", end= '' )
                deleted_str_2 = content.pop(x)
                print(content)   
    with open('with.txt', 'w') as f:
        f.write('\n'.join(content))
        

except Exception as e:
    print( "Error: " + str(e) )
finally:
    print('done')
    f.close()
