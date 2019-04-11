c = open("testing.csv", "r+")

user = str((input("Y/N: "))).upper()
count = 0

inside = c.read()
print(format(inside))

if user == "Y":
    v = [int(input("Number: "))]
    b = [str(input("String: "))]
    print('{}{}'.format(v, b), file=c)
    action = str(input("Print the file content (Y/N): ")).upper()
    if action == "Y":
        content = [str(c.read(0))]
        print(content)
    else:
        print("END")
else:
    # while str(c.read()).isalpha():
    #     count = count + 1
    #     for i in 
    # c = open("testing.csv", "r+")
    content = len(c.readlines())
    inside = str(c.readline(1))
    lim = c.read()

    # print(len(content))
    print(content)
    print(inside)
    print(format(lim))
print("Finish")

c.close()
