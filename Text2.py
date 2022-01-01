class Text:
    def __init__(self,t, q):
        self.text = t
        self.question = q

    def __str__(self):
        return '(Phrase) "'+self.text+'""\n(Question) : "'+self.question+'"' 