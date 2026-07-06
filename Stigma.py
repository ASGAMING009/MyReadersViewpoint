#still learing about this

class Stigma:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return f"[{self.name}]"

    def use(self):
        print(f"You have used the Stigma: {self.name}.")
        print(f"Effect: {self.description}")

# 1. Build the specific Stigma using the blueprint
Uriel_power = Stigma("Hellfire", "Summons the cleansing flames of Eden to burn your enemies to ash.")

Wukong_power = Stigma("Lightning Transformation", "Transforms into a powerful being with enhanced speed and strength.")

Abyssal_power = Stigma("Black Flame", "Unleashes a destructive black flame that incinerates everything in its path.")

Plotter_power = Stigma("[Plotter's Insight]", "Grants a brief glimpse into the hidden variables of the scenario, revealing the best path forward.")

No_power = Stigma("None", "You have no constellation backing you. Rely on your own strength.")

