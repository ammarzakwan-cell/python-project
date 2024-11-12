class Person:
    def setName(self, name: str)-> str:
        self.name = name
        
    def getName(self)-> str:
        return self.name
        
    def splitName(self)-> list[str]:
        return self.name.split()
        
    def setTitleFirstWord(self)-> str:
        _firstWord = True
        _wordList = []
        for word in self.splitName():
            if (_firstWord):
                word = word.title()
                _firstWord = False
                
            _wordList.append(word)
        return ' '.join(_wordList)
            
    
_person = Person()
_person.setName('ammar zakwan')
print(_person.getName())
print(_person.splitName())
print(_person.setTitleFirstWord())
