class FixedDoubleHash:
    def __init__(self, windowSize, content):
        self.h1 = 0
        self.h2 = 0
        self.m = windowSize
        self.s = content
        self.MOD1 = 10**9 + 7
        self.MOD2 = 10**9 + 9

    #WHEN COLLAPSING WINDOW, DROP BEFORE YOU ADD
    def drop(self,i):
        self.h1 -= pow(26*31, self.m-1, self.MOD1)*ord(self.s[i])
        self.h2 -= pow(26*31, self.m-1, self.MOD2)*ord(self.s[i])
        self.h1%=self.MOD1
        self.h2%=self.MOD2

    def add(self, i):
        self.h1 = self.h1 * 26*31 + ord(self.s[i])
        self.h2 = self.h2 * 26*31 + ord(self.s[i])
        self.h1%=self.MOD1
        self.h2%=self.MOD2
    
    def get(self):
        return (self.h1, self.h2)
