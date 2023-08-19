from base_game import CompositeOpenGame

def test_associativity(game1, game2, game3, decisions1, decisions2, decisions3):
    # Create composite games
    comp1_2 = CompositeOpenGame(game1, game2)
    comp_all_left = CompositeOpenGame(comp1_2, game3)
    
    comp2_3 = CompositeOpenGame(game2, game3)
    comp_all_right = CompositeOpenGame(game1, comp2_3)
    
    # Play the games
    utilities_left = comp_all_left.coplay(decisions1 + decisions2 + decisions3)
    utilities_right = comp_all_right.coplay(decisions1 + decisions2 + decisions3)

    # Check if the utilities match
    if utilities_left == utilities_right:
        print(f"Associativity test PASSED for games {game1.name}, {game2.name}, and {game3.name}")
        #return True
    else:
        print(f"Associativity test FAILED for games {game1.name}, {game2.name}, and {game3.name}")
        print(f"Left utility: {utilities_left}, Right utility: {utilities_right}")
        #return False

        
    




def test_identity(game, decisions, trials=1000):
    single_game_utility = game.utility(decisions)
    composite_game = CompositeOpenGame(game, game)
    composite_utility = composite_game.utility(decisions + decisions) / 2
    
    if abs(single_game_utility - composite_utility) < 1e-5:
        print(f"Identity test PASSED for game {game.name}")
    else:
        print(f"Identity test FAILED for game {game.name}. Single utility: {single_game_utility}, Composite utility: {composite_utility}")

def test_distributivity(game1, game2, decisions1, decisions2, trials=1000):
    utility1 = game1.utility(decisions1)
    utility2 = game2.utility(decisions2)
    
    composite_game = CompositeOpenGame(game1, game2)
    composite_utility = composite_game.utility(decisions1 + decisions2)
    
    if abs(utility1 + utility2 - composite_utility) < 1e-5:
        print(f"Distributivity test PASSED for games {game1.name} and {game2.name}")
    else:
        print(f"Distributivity test FAILED for games {game1.name} and {game2.name}. Utility1: {utility1}, Utility2: {utility2}, Composite utility: {composite_utility}")
