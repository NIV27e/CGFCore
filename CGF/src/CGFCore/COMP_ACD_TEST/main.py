from game_implementation import PrisonersDilemma, StagHunt, Chicken
from test_functions import test_identity, test_distributivity, test_associativity

game1 = PrisonersDilemma("PD")
game2 = StagHunt("SH")
game3 = Chicken("CK")
decisions1 = ["cooperate", "cooperate"]
decisions2 = ["stag", "stag"]
decisions3 = ["swerve", "swerve"]

test_identity(game1, decisions1)
test_distributivity(game1, game2, decisions1, decisions2)
test_associativity(game1, game2, game3, decisions1, decisions2, decisions3)
