tr = []

symbols = {"а":"a", "б":"b", "в":"v", "г":"g", "д":"d", "е":"e",
           "ё":"e", "ж":"zh", "з":"z", "и":"i", "й":"y", "к":"k",
           "л":"l", "м":"m", "н":"n", "о":"o", "п":"p", "р":"r",
           "с":"s", "т":"t", "у":"u", "ф":"f", "х":"kx", "ц":"c",
           "ч":"ch", "ш":"sh", "щ":"sch", "ъ":"'", "ы":, "ь":"'",
           "э":"e", "ю":"yu", "я":"ya"}

class Translit:
    def __init__(self, text):
        self.text = text
    def load():
        for i in text:
            s = ""
            for j in i:
                if j in symbol.keys():
                    s += j
            u = s.capitalize()
            tr.append(s)
    return tr
