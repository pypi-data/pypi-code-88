class Item:
    __slots__="value","weight"
    def __init__(self,value,weight):
        self.value = value
        self.weight = weight

def fks(capacity,Items,n):
        a = [0]*n
        sack = [0]*n
        for i in range (0,n):
            a[i] = (Items[i].value/Items[i].weight)
        while a:
            index = a.index(max(a))
            if capacity>Items[index].weight:
                sack[index] = (Items[index].value)
                capacity -= Items[index].weight
                a[index] = -1
            else:
                break
        if a and capacity>0:
            index = a.index(max(a))
            sack[index]=((Items[index].value*capacity)/Items[index].weight)
        return sum(sack)

if __name__ == "__main__":
    a = Item(60,10)
    b = Item(100,20)
    c = Item(120,30)
    A = [a,b,c] 
    print(fks(50,A,len(A)))