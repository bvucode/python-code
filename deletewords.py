#class delete list of words from other list of word

dlist = []

class Deleter:
    def __init__(self, text, text2):
        self.text = text
        self.text2 = text2
    def load(self):
        for i in self.text:
            flag = 1
            for j in self.text2:
                if i == j:
                    flag = 0
                    break
            if flag != 0:
                dlist.append(i)
        return dlist
