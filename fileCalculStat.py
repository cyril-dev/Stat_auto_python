import pandas as pd
import matplotlib.pyplot as plt



class CalculStat():
    def __init__(self,path):
        super().__init__()
        self.path = path
        print(self.path)
        print('Calcul de stat')
        self.data = pd.read_csv(self.path,sep=';')
