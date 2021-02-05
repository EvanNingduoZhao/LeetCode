class solution:
    def newTextEditor(self,operations):
        self.currText=""
        self.clipBoard=""
        self.stack=[]
        def insert(t):
            if not t or len(t)==0:
                return False
            else:
                self.currText+=t
                self.stack.append(('insert',t))
        def undoInsert(t):
            l=len(t)
            self.currText=self.currText[:(l-1)*(-1)]

        def delete():
            if len(self.currText)!=0:
                l=len(self.currText)
                deleted=self.currText[-1]
                self.currText=self.currText[:l-1]
                self.stack.append(('delete',deleted))
        def undoDelete(t):
            self.currText+=t

        def copy(index):
            l=len(self.currText)
            if index>=l:
                return False
            else:
                self.clipBoard=self.currText[index:]
                return True

        def paste():
            if len(self.clipBoard)==0:
                return False
            else:
                self.currText+=self.clipBoard
                self.stack.append(('paste',self.clipBoard[:]))
        def undoPaste(t):
            l = len(t)
            self.currText = self.currText[:(l - 1) * (-1)]

        def undo():
            if self.stack:
                op,t=self.stack.pop()
                if op=='insert':
                    undoInsert(t)
                elif op=='delete':
                    undoDelete(t)
                else:
                    undoPaste(t)
        for operation in operations:
            op=operation.split()[0]
            if len(operation.split())>1:
                t=operation.split()[1]
            if op=="INSERT":
                insert(t)
            elif op=="DELETE":
                delete()
            elif op=="COPY":
                copy(int(t))
            elif op=="PASTE":
                paste()
            else:
                undo()
        return self.currText
operations=["INSERT Code","COPY 0", "INSERT Signal","PASTE", "DELETE",'DELETE',"UNDO"]
s=solution()
print(s.newTextEditor(operations))



