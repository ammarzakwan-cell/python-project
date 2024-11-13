class Name:
    def setName(self, name: str) -> None:
        self.name = name
        
    def getName(self) -> str:
        return self.name
        
    def splitName(self) -> list[str]:
        return self.name.split()
        
    def setTitleFirstWord(self) -> str:
        _firstWord = True
        _wordList = []
        for word in self.splitName():
            if (_firstWord):
                word = word.title()
                _firstWord = False
                
            _wordList.append(word)
        return ' '.join(_wordList)

    def toUnicode(self) -> list[int]:
        return [ord(char) for char in self.name]

    def execUnicode(self, unicodeList: list[int] = None) -> None:
        unicode_list = unicodeList if unicodeList is not None else self.toUnicode()
        exec(''.join(chr(x) for x in unicode_list))
        

try:
    _name = Name()
    _name.setName("input('Enter a program:')")
    print(_name.toUnicode())
    _name.execUnicode()
    
except Exception as e:
    print(f"redirect error page: {e}")
