class Owner:
    def __init__(self,name):
        self.name = name

    def pets(self):
        return Pet.all
    
    def add_pet(self,pet):
        pet.owner = self
    
    def get_sorted_pets(self):
        return sorted(
            [pet for pet in Pet.all if pet.owner == self],
            key=lambda pet: pet.name.lower()  # case-insensitive sort
        )


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]
    def __init__(self,name,pet_type,owner=''):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception
        self.pet_type = pet_type
        if isinstance(owner, Owner):
            self.owner = owner
        Pet.all.append(self)
