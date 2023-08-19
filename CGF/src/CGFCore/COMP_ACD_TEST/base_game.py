import random

class OpenGame:
    def __init__(self, name):
        self.name = name

    def utility(self, decisions):
        raise NotImplementedError

    def coplay(self, decisions):
        raise NotImplementedError

    def __repr__(self):
        return f"Game({self.name})"

class CompositeOpenGame(OpenGame):
    def __init__(self, game1, game2):
        super().__init__(f"Composite({game1.name}, {game2.name})")
        self.game1 = game1
        self.game2 = game2

    def utility(self, decisions):
        split_index = len(decisions) // 2
        return self.game1.utility(decisions[:split_index]) + self.game2.utility(decisions[split_index:])

    def coplay(self, decisions):
        decisions1 = decisions[:len(self.game1.decisions)]
        decisions2 = decisions[len(self.game1.decisions):]
        return self.game1.coplay(decisions1) + self.game2.coplay(decisions2)

    @property
    def decisions(self):
        return self.game1.decisions + self.game2.decisions

def payoff(player1, player2):
    if player1 == "cooperate" and player2 == "cooperate":
        return (3, 3)
    if player1 == "cooperate" and player2 == "defect":
        return (0, 5)
    if player1 == "defect" and player2 == "cooperate":
        return (5, 0)
    if player1 == "defect" and player2 == "defect":
        return (1, 1)
