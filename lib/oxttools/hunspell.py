
import codecs
import unicodedata

class Hunspell(object) :

    def __init__(self, name) :
        self.name = name
        self.words = []

    def addword(self, word) :
        if len(word) :
            dat = unicodedata.normalize('NFC', word) 
            self.words.append(dat)

    def getaff(self) :
        return """
SET UTF-8
"""

    def getdic(self) :
        res = "{}\n".format(len(self.words))
        res += "\n".join(sorted(self.words))
        return res

