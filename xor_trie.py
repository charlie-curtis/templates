class Trie:
    def __init__(self):
        self.nxt = {}
        self.endval = '_END_'
        self.cntval = '_CNT_'

    def getbin(self, x):
        b = ""
        for i in range(45):
            if (1<<i)&x > 0:
                b+="1"
            else:
                b+="0"
        return b[::-1]

    def insert(self, word):
        word = self.getbin(word)
        cur = self.nxt
        for x in word:
            if x not in cur:
                cur[x] = {}
                cur[x][self.cntval] = 0
            cur = cur[x]
            cur[self.cntval]+=1

        if self.endval not in cur:
            cur[self.endval] = 0
        cur[self.endval]+=1

    def remove(self, word):

        word = self.getbin(word)
        cur = self.nxt
        for x in word:
            cur = cur[x]
            cur[self.cntval]-=1
        
        cur[self.endval]-=1

    def maxXor(self, word):

        word= self.getbin(word)
        cur = self.nxt
        out = ""
        for x in word:
            lookingFor = '1' if x == '0' else '0'
            if lookingFor in cur and cur[lookingFor][self.cntval] > 0:
                cur = cur[lookingFor]
                out+=lookingFor
            elif x in cur and cur[x][self.cntval] > 0:
                cur = cur[x]
                out+=x
            else:
                return -1
        return int(out, 2)
