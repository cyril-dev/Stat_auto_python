import pandas as pd
import matplotlib.pyplot as plt
import json



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
        
    def fichierData(self):
        print("Création du fichier data.json")
        with open("data.json","w") as f:
            json.dump(self.dict_data,f,indent=4)