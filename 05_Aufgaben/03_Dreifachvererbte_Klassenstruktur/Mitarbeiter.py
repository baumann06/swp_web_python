from Team import Team

class Mitarbeiter(Team):

    def __init__(self, firmenname, standort, abteilungs_id, abteilungsname,
                 team_id, teamname, mitarbeiter_id, mitarbeitername):

        super().__init__(firmenname, standort, abteilungs_id, abteilungsname,
                         team_id, teamname)

        self.mitarbeiter_id = mitarbeiter_id
        self.mitarbeitername = mitarbeitername

    def __str__(self):
        return f"{super().__str__()}, Mitarbeiter: {self.mitarbeitername} (ID {self.mitarbeiter_id})"