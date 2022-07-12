import json
import os
import logging

from constants import CUR_DIR

LOGGER = logging.getLogger()


class Liste(list):
      
    def __init__(self, name):
        self.name = name   

    def add_element(self, element: str) -> bool:               
       
        if not isinstance(element, str):
            raise ValueError("Vous ne pouvez ajouter que des chaînes de caractères!")

        if element in self:
            LOGGER.error(f"{element} est déjà dans la liste")
            return False

        self.append(element)             
        return True

    def remove_element(self, element: str) -> bool:       
        if element in self:
            self.remove(element)
            return True       
        print(f"{element} n'est pas dans la liste !")       
        return False

    def show_liste(self):
        print(f"{self.name} :")
        for element in self:
            print(f" - {element}")

    def clear_liste(self):
        if self==[]:
            print('La liste est déjà vide !')
        else:
            self.clear()           
            print("La liste a été vidée ...")  

    def __file_access__(self):  
        chemin=os.path.join(CUR_DIR, f"{self.name}.json")   
        #Vérifie si le fichier existe et le crée si besoin
        if not os.path.exists(chemin):
            f=open(chemin,"w+")  
            json.dump([],f)   
            f.close()
        return chemin

    def load_data(self):
        chemin=self.__file_access__()              
        with open(chemin, 'r') as f:
            print(self.name)  
            return(json.loads(f.read()))  

    def save_data(self):     
        chemin=self.__file_access__()
        #écriture dans le fichier des données
        with open(chemin, 'w') as f:           
            json.dump(self, f, indent=4)        
        return True
