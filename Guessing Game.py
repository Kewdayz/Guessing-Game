import os
import matplotlib.pyplot as plt
lst = []
lsth = []
n = 100
a = int(input("What is the secret number between 1 - 100: "))
os.system('cls')

for i in range(0, n):
    b = int(input("what is the number between 1 and 100: "))

    lst.append(b)
    lsth.append("#" * b)
    break

print("#" * b)

while True:
    if b > a:
        print("lower")
        for i in range(0, n):
            b = int(input(""))
            lst.append(b)
            lsth.append("#" * b)
            print("#" * b)

            break

    elif a == b:

        print("YOU GOT IT    " * 3)
        print("Your guesses:")
        print(lst)
        p = len(lst)
        print("How many times u guessed:")
        print(p)

        with open('output.txt', 'w') as file:
            for output in lst:
                file.write("%i\n" % output)
        with open('outputhash.txt', 'w') as filehandle:
            for listitem in lsth:
                filehandle.write('%s\n' % listitem)
        tg = [x for x in range(len(lst))]
        plt.scatter(tg,lst, label='scatter plot', color='b', s=50)

        plt.xlabel('Guesses')
        plt.ylabel('number guessed')

        plt.title('Scatter plot chart\nof your choices')
        plt.show()
        break
    else:
        print("higher")
        for i in range(0, n):
            b = int(input(""))
            lst.append(b)
            lsth.append("#" * b)
            print("#" * b)
            break
