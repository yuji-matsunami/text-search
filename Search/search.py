class Search:
    def __init__(self, text, key):
        self.text = text
        self.key = key
        self.text_l = len(text)
        self.key_l = len(key)
    def search(self):
        pass


class SimpleSearch(Search):
    def __init__(self, text, key):
        super().__init__(text, key)

    def search(self):
        cnt = 0 # 参照回数を記録
        for i in range(self.text_l-self.key_l+1):
            for j in range(self.key_l):
                cnt += 1
                if self.text[i+j] != self.key[j]:
                    break
            print(i)
        print("cnt:", cnt)

class BM(Search):
    def __init__(self, text, key):
        super().__init__(text, key)
        self.skip = self.make_skip_func()

    def make_skip_func(self):
        skip = {}
        for i in range(ord("A"), ord("Z")+1):
            skip[i] = self.key_l
        for i in range(ord("a"), ord("z")+1):
            skip[i] = self.key_l
        for i in range(self.key_l-1):
            skip[ord(self.key[i])] = self.key_l - i - 1
        return skip
    
    def skip_func(self, s):
        if ord(s) not in self.skip:
            return self.key_l
        else:
            return self.skip[ord(s)]

    def search(self):
        cnt = 0 # 参照回数を記録
        pos = self.key_l - 1
        while pos < self.text_l:
            cnt += 1
            if self.text[pos] == self.key[self.key_l-1]:
                k = pos - 1
                j = self.key_l - 2
                while j >= 0 and self.text[k] == self.key[j]:
                    cnt += 1
                    k -= 1
                    j -= 1
                if j == 0:
                    print(k+1)
            pos = pos + self.skip_func(self.text[pos])
        print("cnt", cnt)