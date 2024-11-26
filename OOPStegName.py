class Name:
    def setName(self, name: str) -> None:
        self.name = name
        
    def getName(self) -> str:
        return self.name
        
    def splitName(self) -> list[str]:
        return self.name.split()
        
    def setTitleFirstWord(self) -> str:
        # can set self.splitName()[0] ... blablabla 
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

    def toChr(self, unicodeList: list[int] = None) -> str:
        unicode_list = unicodeList if unicodeList is not None else self.toUnicode()
        return ''.join(chr(x) for x in unicode_list)
        
    def execUnicode(self, unicodeList: list[int] = None) -> None:
        exec(self.toChr(unicodeList))
        
    def sandbox(self) -> str:
        return "sandbox api test"
        
try:
    _name = Name()
    _name.setName("print(_name.sandbox())")
    print(_name.toUnicode())
    print(_name.toChr([105, 109, 112, 111, 114, 116]))
    # can accept parameter to overwrite name
    _name.execUnicode(_name.toUnicode())
    _name.execUnicode()
    
except Exception as e:
    print(f"redirect error page: {e}")




