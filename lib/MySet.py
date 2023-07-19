class MySet:
    def __init__(self,enumerables=[]):
        self.dictionary = {}
        for value in enumerables:
            self.dictionary[value] = True
            
    def has(self,value):
        return value in self.dictionary
    
    def add(self,value):
        self.dictionary[value] = True
        return self
    
    def delete(self,value):
        self.dictionary.pop(value,None)
        return self
    
    def size(self):
        return len(self.dictionary)
