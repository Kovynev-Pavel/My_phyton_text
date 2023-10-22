class Checker():
    def chek(self, text):
        f = open("pon3.txt", "r")
        bad_words = f.read()
        text = text.lower()
        text = text.replace(",", "")
        text = text.replace(":", "")
        text = text.replace(".", "")
        text = text.replace("!", "")
        text = text.replace("?", "")
        text = text.replace("...", "")
        text = text.replace("-", "")
        text = text.replace("_", "")
        text = text.replace(")", "")
        text = text.replace("(", "")
        text = text.replace(";", "")
        splitted_text = text.split()
        for word in splitted_text:
            if word in bad_words:
                print(True)
            else:
                print(False)
        f.close()
checker = Checker()
checker.chek("Я сделал папе сливу, я молодец")