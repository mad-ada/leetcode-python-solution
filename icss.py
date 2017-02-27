import numpy as np
import pandas as pd

class ChangePoints:
    def __init__(self, series, cp=None, num_of_cp=0):
        self.series = series
        self.cp = []
        self.num_of_cp = 0

    def ICSS(self, st, en, D_star):
        first = st
        last = en

        [M_value, loc] = calculate_M(first, last)
    
    def calcuate_M(self, st, en):
        sub_series = self.series[st:en]
        len = en - st

        C_k = []
        D_k = []

        for i in range(0, len):
            C_k.append(np.sum(sub_series[x]**2 for x in range(0, i+1)))

        for i in range(0, len):
            D_k.append((C_k[i] / C_k[len - 1]) - ((i + 1) / len))

        tmp = np.sqrt(len / 2) * np.absolute(D_k)
        M_value = np.max(tmp)
        loc = np.argmax(tmp)
        return [M_value, loc]
