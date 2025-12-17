from Abteilung import Abteilung

class Team(Abteilung):

    def __init__(self, firmenname, standort, abteilungs_id, abteilungsname,
                 team_id, teamname):

        super().__init__(firmenname, standort, abteilungs_id, abteilungsname)

        self.team_id = team_id
        self.teamname = teamname

    def __str__(self):
        return f"{super().__str__()}, Team: {self.teamname} (ID {self.team_id})"
