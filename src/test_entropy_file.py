import pickle

def main():
    first_entropy_file = "./en/first_entropy.data"

    with open(first_entropy_file, "rb") as f:
        lis = pickle.load(f)

    voc = open("./en/five.txt").read().split()
    mini = max(range(len(lis)), key=lambda x:lis[x])
    print(mini)
    print(voc[mini])

    return

if __name__ == '__main__':
    main()
    