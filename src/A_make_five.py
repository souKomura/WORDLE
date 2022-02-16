def make_five(lang="en"):
    """
    語彙ファイルから5文字で構成される単語の抽出．
    """
    readfrom = "./{}/words.txt".format(lang)
    writeto = "./{}/five.txt".format(lang)
    lis = []
    with open(readfrom) as f:
        for row in f.readlines():
            row = row.strip()
            if len(row) == 5 and (lang=="jp" or row.isalpha()):
                lis.append(row.lower())
    
    lis = sorted(list(set(lis)))

    with open(writeto, "w") as f:
        for w in lis:
            f.write(w)
            f.write("\n")
    


if __name__ == '__main__':
    make_five()
    