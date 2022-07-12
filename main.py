from liste import Liste

choice=""
separator="="
actions=["1 = Ajouter un élément à la liste",
         "2 = Retirer un élément de la liste",
         "3 = Afficher les éléments de la liste",
         "4 = Vider la liste",
         "5 = Quitter"]

liste = Liste("Liste de Courses")

#chargement des données si elles existent
data_load_from_file=liste.load_data()

for i in range(len(data_load_from_file)):
    liste.add_element(data_load_from_file[i].upper())

#boucle principale
while choice!= "5": 
          
    #affichage du menu
    print(f"""\n {separator*13} {liste.name} {separator*13}""")

    for i in range(len(actions)):
        print(f"""{actions[i]}""")  
    
    print(f"{separator*29}{len(liste.name)*separator}")
    choice=input(f"""\U0001F914 Votre choix ? : 
    """)    

    #en fonction des choix 1 à 4
         
    if choice =='1':                       
        element_to_add=input("Que voulez-vous ajouter à la liste ? : ")   
        liste.add_element(element_to_add.upper())   

    if choice =='2': 
        if len(liste)==0:             
            print("La liste est vide !")
        else:
            element_to_remove=input("Que voulez-vous retirer de la liste ? : ")
            liste.remove_element(element_to_remove) 

    if choice =='3': 
        liste.show_liste()   
        if len(liste)==0:             
            print("La liste est vide !") 

    if choice =='4': 
        liste.clear_liste()    

liste.save_data()  
print("\n Au revoir !")    