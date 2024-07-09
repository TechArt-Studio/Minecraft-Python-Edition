all_biomes = ["forest", "desert", "ocean", "taiga", "mountains", "big_mountains"]


def getBiomeByTemp(temp):
    print(temp)
    """
     9:0.7
    =1:0.77777777777777777777777777777777777777777777777777
    """
    # if 50 > temp > 3.57
    if temp > 30:
        return all_biomes[2]
    if 30 >= temp > 20:
        return all_biomes[1]  # Desert
    if 20 >= temp > 10:
        print(f"{temp} is Forest")
        return all_biomes[0]  # Forest
    if 10 >= temp >= 0:
        return all_biomes[3]  # Taiga
    if 0 >= temp > -25:
        return all_biomes[4]  # mountains
    if -25 >= temp >= 120:
        return all_biomes[5]  # bIg mountains
    # return all_biomes[2]  # Taiga


class Biomes:
    def __init__(self, biome):
        self.biome = biome

    def getBiomeGrass(self):
        if self.biome == "desert":
            return "sand"
        if self.biome == "ocean":
            return "water"
        if self.biome == "forest" :
            return "grass"
        if self.biome == "taiga":
            return "grass"
        if self.biome == "mountains":
            return "grass"
        if self.biome == "big_mountains":
            return "stone"
        return "grass"

    def getBiomePlant(self):
        if self.biome == "desert":
            return "cactus"

    def getBiomeDirt(self):
        if self.biome == "desert":
            return "sand"
        if self.biome == "forest" or self.biome == "taiga" or self.biome == "mountains" \
                or self.biome == "big_mountains":
            return "dirt"
        if self.biome == "ocean":
            return "water"
        return "dirt"

    def getBiomeStone(self):
        if self.biome == "desert":
            return "sandstone"
        if self.biome == "forest" or self.biome == "taiga" or self.biome == "mountains":
            return "stone"
        if self.biome == "ocean":
            return "gravel"
        if self.biome == "big_mountains":
            return "stone"
        return "stone"
