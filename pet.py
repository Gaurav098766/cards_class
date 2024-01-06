# class Pet:
#     allowed = ['cat','dog','fish','rat']
#     def __int__(self,name,species):
#         if species not in Pet.allowed:
#             raise ValueError(f"You cannot have {species} as pet")
#         self.name = name
#         self.species = species

#     def set_species(self,species):
#         if species not in Pet.allowed:
#             raise ValueError(f"You cant have a {species} pet!")
#         self.species =species

# cat = Pet("Blue","cat")
# dog = Pet("Wyatt","dog") 

class Chicken:

    total_eggs = 0;

    def __init__(self,species,name,eggs=0):
        self.species = species
        self.name = name
        self.eggs = eggs

    def lay_egg(self):
        self.eggs +=1;
        Chicken.total_eggs +=1;
        return self.eggs
    
