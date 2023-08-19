from base_game import OpenGame,payoff
class PrisonersDilemma(OpenGame):
    def __init__(self,name):
        self.name = name
        self.decisions = ["cooperate", "defect"]
    
    def utility(self, decisions):
        p1, p2 = payoff(decisions[0], decisions[1])
        return p1

    def coplay(self, decisions):
        p1, p2 = payoff(decisions[0], decisions[1])
        return p2

class StagHunt(OpenGame):
    def __init__(self,name):
        self.name = name
        self.decisions = ["stag", "hare"]

    def utility(self, decisions):
        if decisions == ["stag", "stag"]:
            return 3
        if decisions == ["stag", "hare"] or decisions == ["hare", "stag"]:
            return 0
        if decisions == ["hare", "hare"]:
            return 2
        raise ValueError(f"Invalid decision combination: {decisions}")

    def coplay(self, decisions):
        if decisions == ["stag", "stag"]:
            return 3
        if decisions == ["stag", "hare"]:
            return 2
        if decisions == ["hare", "stag"]:
            return 2
        if decisions == ["hare", "hare"]:
            return 2
        raise ValueError(f"Invalid decision combination: {decisions}")

class Chicken(OpenGame):
    def __init__(self,name):
        self.name = name
        self.decisions = ["swerve", "straight"]

    def utility(self, decisions):
        if decisions == ["swerve", "swerve"]:
            return 0
        if decisions == ["swerve", "straight"] or decisions == ["straight", "swerve"]:
            return 1
        if decisions == ["straight", "straight"]:
            return -1
        raise ValueError(f"Invalid decision combination: {decisions}")

    def coplay(self, decisions):
        if decisions == ["swerve", "swerve"]:
            return 0
        if decisions == ["swerve", "straight"]:
            return -1
        if decisions == ["straight", "swerve"]:
            return -1
        if decisions == ["straight", "straight"]:
            return -1
        raise ValueError(f"Invalid decision combination: {decisions}")