class Team:
    def __init__(self, name, project, position):
        self.name = name
        self.project = project
        self.position = position
        print(self)

    def __str__(self):
        return f"-- Developer létrehozva. --\n " \
               f"{self.name} a {self.project}-en dolgozik {self.position} szerepkörben."

team = []

team.append(Team("Ricsi", "SolArch", "Frontend"))
team.append(Team("Angéla", "ZerTeng", "Tesztelő"))
team.append(Team("Peti", "KefERP", "Backend"))
team.append(Team("Éva", "KefERP", "Frontend"))

for x in team:
    for y in team:
        if x.project == y.project:
            if x.name > y.name and x.name != y.name:
                print(f"\n{x.name} és {y.name} dolgoznak egy projekten.")