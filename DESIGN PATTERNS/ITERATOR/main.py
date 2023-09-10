class FootballTeamIterator:
    def __init__(self,members):
        self.memebers = members
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.memebers):
            val = self.memebers[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration()
