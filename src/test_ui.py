import os

def main():
    lis = ["{}".format(i)*4 for i in range(10)]
    lis2 = ["🟨🟩🟨⬛️🟨" for _ in range(3)]

    os.system("clear")
    esc = "\033["

    for i, state in enumerate(lis2):
        print("{0}{1};1H{2}".format(esc,i+2,state))
    
    for i, n in enumerate(lis):
        print("{0}{1};15H{2}".format(esc,i+2,n))

    return

if __name__ == '__main__':
    main()
    