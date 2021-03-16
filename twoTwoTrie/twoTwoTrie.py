

class node:
    def __init__(self,data=None):
        self.children = {}
        self.interesting = False

    def add_child(self,data):
        return self.children.setdefault(data,node())
        
def count2pow(origin,a_rev):
    count = 0
    for i in range(len(a_rev)):
        at = origin
        index = i
        ch = a_rev[index]
        while ch in at.children:
            at = at.children[ch]
            if at.interesting:
                count+=1
            index +=1 
            try:
                ch = a_rev[index]
            except IndexError:
                break
    return count
    
origin = None       # global (1)
testcases = {}      # global (2)

def twoTwo(a):
    a_rev = list(a[::-1])
    global origin
    global testcases
    if not origin:
        origin = node()
        num = 1
        for _ in range(800):
            at = origin
            for char in str(num)[::-1]:
                at = at.add_child(char)
            num<<=1
            at.interesting = True
            
    if a in testcases:
        return testcases[a]
    else:
        count = count2pow(origin,a_rev)
        testcases[a] = count
        return count
    
            
if __name__ == '__main__':
    t = 10
    fil = open('test.txt')
    inp = fil.read()
    fil.close()
    inp = inp.split()
    result = []
    for t_itr in inp:
        a = t_itr
        result.append(twoTwo(a))
    print('\n'.join(list(map(str,result))))


