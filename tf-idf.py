import math

class Tfidf:
    """tf, idf, tf-idf with n-grams"""
    def __init__(self, getlist, tfidf = "tf-idf", ngrams = 1):
        self.getlist = getlist
        self.tfidf = tfidf
        self.ngrams = ngrams

    def indexing(self, arg):
        """memoization"""
        self.arg = arg
        self.ind = 0
        memo = {}
        for i in self.arg:
            if i not in memo.keys():
                memo[i] = 1
            else:
                memo[i] = memo[i] + 1
        return memo

    def fngrams(self, text, ngram):
        self.text = text
        self.ngram = ngram
        nlist = []
        for i in self.text:
            trlist = []
            for x, j in enumerate(i):
                tc = ""
                tx = x
                for k in range(self.ngram):
                    if k == 0:
                        tc = str(i[tx])
                    elif k > 0:
                        try:
                            tc += " " + str(i[tx])
                        except IndexError:
                            break
                    trlist.append(tc)
                    tx += 1
            nlist.append(trlist)
        return nlist

    def load(self):
        """method return dictionary of words with tf, idf, tf-idf with n-grams"""
        kdict = {}
        instv = []
    
        if self.ngrams > 1 and self.ngrams <= 4:
            glist = self.fngrams(self.getlist, self.ngrams)
            for i in glist:
                for j in i:
                    instv.append(j)
            self.getlist = glist.copy()

        elif self.ngrams == 1:
            for i in self.getlist:
                for j in i:
                    instv.append(j)

        ind = self.indexing(instv)

        if self.tfidf == "tf" and len(self.getlist) != 1:
            for i in self.getlist:
                for j in i:
                    c = ind[j]
                    kdict[j] = c / len(instv)
            return kdict

        elif self.tfidf == "idf" and len(self.getlist) != 1:
            for i in self.getlist:
                for j in i:
                    if j not in kdict:
                        kdict[j] = math.log10(len(self.getlist)/sum([1.0 for i in self.getlist if j in i]))
            return kdict

        elif self.tfidf == "tf-idf" and len(self.getlist) != 1:
            for i in self.getlist:
                for j in i:
                    if j not in kdict.keys():
                        c = ind[j]
                        vartf = c / len(instv)
                        varidf = math.log10(len(self.getlist)/sum([1.0 for i in self.getlist if j in i]))
                        kdict[j] = vartf * varidf
            return kdict
