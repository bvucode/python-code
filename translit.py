trlist = []

symbols = {"а":"a", "б":"b", "в":"v", "г":"g", "д":"d", "е":"e",
           "ё":"e", "ж":"zh", "з":"z", "и":"i", "й":"y", "к":"k",
           "л":"l", "м":"m", "н":"n", "о":"o", "п":"p", "р":"r",
           "с":"s", "т":"t", "у":"u", "ф":"f", "х":"kx", "ц":"c",
           "ч":"ch", "ш":"sh", "щ":"sch", "ъ":"'", "ы":"y", "ь":"'",
           "э":"e", "ю":"yu", "я":"ya"}

class Translit:
    def __init__(self):
        pass
    def load(self, text):
        self.text = text
        s = ""
        for i in self.text:
            if i in symbols.keys():
                s += symbols[i]
            else:
                s += i
        trlist.append(s)
        return trlist
