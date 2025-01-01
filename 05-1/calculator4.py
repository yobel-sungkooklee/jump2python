# calculator3.py
class FourCal:
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        return self.first+self.second
    def mul(self):
        result=self.first * self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result= self.first/self.second
        return result
    
    

a=FourCal()
a.setdata(4,2)
#FourCal.setdata(a,5,2)
b=FourCal()
b.setdata(3,8)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

print(b.add())
print(b.sub())
print(b.mul())
print(b.div())
