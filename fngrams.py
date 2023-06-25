def fngrams(text, ngrams):
    """ function to make n-grams"""
    nlist = []
    for i in text:
        for x, j in enumerate(i):
            trlist = []
            tc = ""
            tx = x
            for k in range(ngrams):
                if k == 0:
                    tc = str(i[tx])
                elif k > 0:
                    try:
                        tc += " " + str(i[tx])
                    except IndexError:
                        break
                trlist.append(tc)
                tx += 1
            nlist.append(tuple(trlist))
    return nlist
print(fngrams([["pyhon", "awesome", "programming", "language"]], 3))
