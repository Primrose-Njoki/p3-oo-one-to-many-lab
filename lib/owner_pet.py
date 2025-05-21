class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]
    def __init__(self,name,pet_type,owner=None):
      self.name=name
      self.pet_type=pet_type
      self.owner=owner
      Pet.all.append(self)
        #valideate pet_type
      if pet_type not in Pet.PET_TYPES:
         raise  Exception('lol')
      self.pet_type=pet_type
      pass

class Owner:
    def __init__(self,name):
        self.name=name

    
    def pets(self) :
        return [pet for pet in Pet.all if pet.owner==self]
    def add_pet(self,pet):
        if not isinstance(pet,Pet):
            raise TypeError ("Piiik")
        pet.owner=self

    def get_sorted_pets(self):
        #if not hasattr(self, 'name') or not isinstance(self.name, str):
            #raise ValueError("Invalid Owner instance")
        return sorted(self.pets(), key=lambda pet: pet.name)
        
pass
pass
cate =Owner("cate")
dog=Pet("rose",'dog',cate)


cate.add_pet(dog)
print (dog.owner.name)
sorted_pets = cate.get_sorted_pets()
print("Cate's pets sorted:", [pet.name for pet in sorted_pets])