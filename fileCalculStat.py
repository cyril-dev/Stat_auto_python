import pandas as pd
import matplotlib.pyplot as plt




class CalculStat():

    dict_data = {}
    
    def __init__(self,path):
        super().__init__()
        self.path = path
        print(self.path)
        self.data = pd.read_csv(self.path,sep=',')
    
    def contenuFile(self):
        list_colonnes = {}
        print("##################################")
        print("Contenu du fichier")
        print("##################################\n")
        print("Nombre d'entrées :",len(self.data.index))
        self.dict_data["Nombres d'entrées"] = len(self.data.index)
        print("Nombre d'items :",len(self.data.columns))
        self.dict_data["Nombre d'items"] = len(self.data.columns)
        print("")
        print("Liste des colonnes du fichiers\n")
        for co in self.data:
            print(" -- "+co)
            list_colonnes[co] = co
        print("")
        print("----------------------------------\n")
        self.dict_data["liste des colonnes"] = list_colonnes
        return self.dict_data

    def meanByItem(self,item):
        return self.data[item].value_counts().mean()
    
    def diaCirculaire(self,item):
        """_summary_

        Args:
            item (string): _description_
        """
        plt.pie(self.data[item].value_counts())
        plt.savefig("DiaCirculaire_"+item+".png")

    def resumeItem(self,item,value,item2):
        """_summary_

        Args:
            item (String): _description_
            value (string): _description_
            item2 (string): _description_
        """
        data10 = self.data.loc[self.data[item] == value]
        data10[item2].value_counts()
        
    