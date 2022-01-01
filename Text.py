class Text:
    """Un text du recit"""
    def __init__(self,t, q):
        self.text = t
        self.questions = q

    def __str__(self):
        return "(Phrase) \""+self.text+"\"\n(Question) : \""+self.questions+"\""