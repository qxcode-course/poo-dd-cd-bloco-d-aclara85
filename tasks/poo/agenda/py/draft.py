class Fone:
    def __init__(self, id, number):
        self.id = id
        self.number = number
    
    def isValid(self):
        validos = "0123456789().-"
        return all(c in validos for c in self.number)
    
    def __str__(self):
        return f"{self.id}:{self.number}"
    
class Contact:
    def __init__(self,name):
        self.name = name
        self.fones = []
        self.favorited = False

    def addFone (self, id, number):
        f = Fone(id, number)
        if f.isValid():
            self.fones.append(f)
        else:
            return
    
    def rmFone(self, index):
        if 0 <= index < len(self.fones):
            self.fones.pop(index)
    
    def toogleFavorited(self):
        self.favorited = not self.favorited
    
    def isFavorited(self):
        return self.favorited
    
    def __str__(self):
        fones_str = ", ".join(str(f) for f in self.fones)
        prefix = "@ " if self.favorited else "- "
        return prefix + self.name + " [" + fones_str + "]"
    
class Agenda:
    def __init__(self):
        self.contacts = []

    def findPosByName(self, name):
        for i, c in enumerate(self.contacts):
            if c.name == name:
                return i
        return -1
    
    def getContact(self, name):
        pos = self.findPosByName(name)
        if pos != -1:
            return self.contacts[pos]
        return None
    
    def addContact(self, name, fones):
        pos = self.findPosByName(name)
        if pos == -1:
            cont = Contact(name)
            for id, num in fones:
                cont.addFone(id, num)
            self.contacts.append(cont)
        else:
            cont = self.contacts[pos]
            for id, num in fones:
                cont.addFone(id, num)
        
        self.contacts.sort(key=lambda x: x.name)
    
    def rm(self, name):
        pos = self.findPosByName(name)
        if pos != -1:
            self.contacts.pop(pos)
    
    def search(self, pattern):
        pattern = pattern.lower()
        for contato in sorted(self.contacts, key=lambda x: x.name):
            
            if pattern in contato.name.lower():
                print(contato)
                continue
            
            for f in contato.fones:
                if pattern in f.id.lower() or pattern in f.number:
                    print(contato)
                    break
    
    def getFavorited(self):
        favs = []
        for contato in sorted(self.contacts, key=lambda x: x.name):
            if contato.isFavorited():
                favs.append(contato)
        return favs

    def __str__(self):
        return "\n".join(str(c) for c in self.contacts)

def main():
    agenda = Agenda()

    while True:
        line = input().strip()
        print("$" + line)
        if line == "end":
            break

        parts = line.split()
        cmd = parts[0]

        if cmd == "add":
            name = parts[1]
            fones = []
            for par in parts[2:]:
                id, num = par.split(":")
                fones.append((id, num))
            agenda.addContact(name, fones)
        
        elif cmd == "rmFone":
            name = parts[1]
            index = int(parts[2])
            pos = agenda.findPosByName(name)
            if pos != -1:
                agenda.contacts[pos].rmFone(index)
        
        elif cmd == "rm":
            name = parts[1]
            agenda.rm(name)
        
        elif cmd == "search":
            pattern = parts[1]
            agenda.search(pattern)
        
        elif cmd == "tfav":
            name = parts[1]
            pos = agenda.findPosByName(name)
            if pos != -1:
                agenda.contacts[pos].toogleFavorited()
        
        elif cmd == "favs":
            for c in agenda.getFavorited():
                print(c)

        
        elif cmd == "show":
            print(agenda)
main()
