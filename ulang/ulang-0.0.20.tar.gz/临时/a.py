class C1:
    class C2:
        def __init__(self):
            print("c2")
        
    def __init__(self):
        print("c1")
C1()
C1.C2()