def fngrams(text, ngrams):
    """ function to make n-grams"""
    nlist = []
    for i in text:
        for x, j in enumerate(i):
            trlist = []
            tc = ""
            for k in range(ngrams):
                if k == 0:
                    tc = str(i[x + k])
                elif k > 0:
                    try:
                        tc += " " + str(i[x + k])
                    except IndexError:
                        break
                trlist.append(tc)
            nlist.append(tuple(trlist))
    return nlist
print(fngrams([["pyhon", "awesome", "programming", "language"]], 3))
