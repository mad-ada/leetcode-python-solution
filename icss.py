import numpy as np
import pandas as pd

class ChangePoints:
    def __init__(self, series, D_star, cp=None, num_of_cp=0):
        self.series = series
        self.D_star = D_star
        self.cp = []
        self.num_of_cp = 0

    def ICSS(self, st, en):
        first = st
        last = en

        [M_value, loc] = self.calculate_M(first, last)
        tmp_loc = loc

        if M_value >= self.D_star:
            #step 2a
            last = loc + 1
            while True:
                [M_value, loc] = self.calculate_M(first, last)
                if M_value < self.D_star:
                    break
                else:
                    last = loc + 1
            kfirst = last
            
            #step 2b
            first = tmp_loc + 1
            last = en
            while True:
                [M_value, loc] = self.calculate_M(first, last)
                if M_value < self.D_star:
                    break
                else:
                    frist = loc + 1
            klast = first - 1

            #step 2c
            if kfirst == klast:
                self.num_of_cp += 1
                self.cp.append(kfirst)
            else:
                self.num_of_cp += 1
                self.cp.append(kfirst)
                self.num_of_cp += 1
                self.cp.append(klast)
                self.ICSS(kfrist + 1, klast + 1)

    def eliminate(self):
        _cp = []
        _cp.append(0)
        for x in range(0, len(self.cp)):
            _cp.append(self.cp[x])
        
        _cp.append(len(self.series))

        flag = 1
        iterations = 0

        while flag:
            num_of_cp_new = 0
            cp_new = []
            iterations += 1
            
            for i in range(1, self.num_of_cp + 1):
                first = _cp[i-1] + 1
                last = _cp[i+1]

                [M_value, loc] = self.calculate_M(first, last)
                if M_value >= self.D_star:
                    num_of_cp_new += 1
                    cp_new.append(loc)

            cp_new = list(set(cp_new))
            cp_new.sort()
            num_of_cp_new = len(cp_new)

            if self.num_of_cp == num_of_cp_new:
                n = 0
                for i in range(0, self.num_of_cp):
                    if np.absolute(_cp[i+1] - _cp[i]) <= 2:
                        n += 1

                if n == self.num_of_cp:
                    flag = 0

            if iterations >= 20:
                flag = 0

        self.cp = cp_new


    def calculate_M(self, st, en):
        sub_series = self.series[st:en]
        len = en - st

        C_k = []
        D_k = []

        for i in range(0, len):
            C_k.append(np.sum(sub_series[x]**2 for x in range(0, i+1)))

        for i in range(0, len):
            D_k.append((C_k[i] / C_k[len - 1]) - ((i+1) / len))

        tmp = np.sqrt(len / 2) * np.absolute(D_k)
        M_value = np.max(tmp)
        idx = np.argmax(tmp)
        loc = st + idx
        return [M_value, loc]
    #temp
    def fourier_transform(series):
        f, Pxx_den = signal.periodogram(series)
        df = pd.DataFrame(data=f, index=Pxx_den)
        df.sort_index(ascending=False, inplace=True)
        top2 = df.head(n=2)
        period = np.min(1.0/top2[:])
    return period
