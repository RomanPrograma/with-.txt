
try:
    with open('with.txt', 'r') as f:
         content = f.read()
         lines = set()
         for line in content.split():
            if line in lines:
                print('File contains duplicate lines')
                break
            lines.add(line)
         else:
            print('File does not contain duplicate lines')
except Exception as e:
    print(e)
finally:
    print('Execution completed')
    f.close()