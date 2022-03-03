import pandas as pd
import matplotlib.pyplot as plt
import os




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
        """Descristion

        Args:
            item (string): _description_

        Returns:
            String: chemin de l'image du diagramme
        """
        namefile = "DiaCirculaire_"+item+".png"

        plt.pie(self.data[item].value_counts(),autopct='%1.1f%%',shadow=True, startangle=90)
        #self.data[item].value_counts().plot(kind='pie')
        plt.legend(self.data[item].value_counts().index.tolist(),title=item,loc="lower left",bbox_to_anchor=(0.75, -0.15, 1, 1.5))
        plt.savefig(namefile)
        return os.path.join(os.path.dirname(__file__), namefile)
        

    def resumeItemByVar(self,item,value,item2):
        """_summary_

        Args:
            item (String): _description_
            value (string): _description_
            item2 (string): _description_
        """
        data10 = self.data.loc[self.data[item] == value]
        data10[item2].value_counts()

    def resumeItem(self,item):
        return self.data[item].value_counts().to_dict()