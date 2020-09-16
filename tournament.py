class Tournament():
    def __init__(self,title=None,date=None,teilnehmer=None,tType=''):
        self.title=title
        self.date=date
        self.teilnehmer= teilnehmer if teilnehmer!=None else []
        self.tType=tType
