class Bacterium:

    def __init__(self, shape, respiration, presence, reproduction="Binary Fussion"):
        self.shape = shape
        self.respiration = respiration
        self.presence = presence
        self.reproduction = reproduction
        self.category = "Prokaryotes"

    def print_bacteria(self):
        print(f"Bacteria shape : {self.shape}\nrespiration shape : {self.respiration}\nBacterial Presence {self.presence}\nBacterial Reproduction : {self.reproduction}\nBacterial catagory : {self.category}")


print("-----------------Information about first bacteria-------------------")
bacteria_one = Bacterium("Bacillus", "Obligate Aerobic", "Diplo")
bacteria_one.print_bacteria()
print("--------------------------------------------------------------------")

print("-----------------Information about second bacteria-------------------")
bacteria_two = Bacterium("Coccus", "Obligate Aerobic", "Strepto")
bacteria_two.print_bacteria()
print("--------------------------------------------------------------------")

print("-----------------Information about third bacteria-------------------")
bacteria_three = Bacterium("Spirillum", "obligate Anaerobic", "Diplo")
bacteria_three.print_bacteria()
print("--------------------------------------------------------------------")
