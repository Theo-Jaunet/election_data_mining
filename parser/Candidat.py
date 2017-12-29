class Candidat:

    def __init__(self, name, vote):
        self.name = name.replace("'", "\'")
        self.vote = vote

    def __str__(self):
        return '{nom:"' + self.name + '", vote:' + self.vote + '}'
