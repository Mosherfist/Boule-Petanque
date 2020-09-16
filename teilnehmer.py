class Teilnehmer():
    def __init__(self,name=None, age=0, active=True):
        self.name=name
        self.age=age
        self.active=active
    
    @property
    def active(self):
        return self.active
    @active.setter
    def active(self, val):
        self.active=val
    
 