def checkVerticalConnection(state, key):
    accumulatedValue = 0
    if state.board.get((key[0], key[1])) == state.to_move:
        if state.board.get((key[0], key[1]+1)) == state.to_move:
            accumulatedValue += 5
            if state.board.get((key[0], key[1]+2)) == state.to_move:
                accumulatedValue += 10
                if state.board.get((key[0], key[1]+3)) == state.to_move:
                    accumulatedValue += 1000
    if state.board.get((key[0], key[1])) == "O":
        if state.board.get((key[0], key[1]+1)) == "O":
            accumulatedValue -= 5
            if state.board.get((key[0], key[1]+2)) == "O":
                accumulatedValue -= 10
                if state.board.get((key[0], key[1]+3)) == "O":
                    accumulatedValue -= 5000
    return accumulatedValue


def checkHorizontalConnection(state, key):
    accumulatedValue = 0
    if state.board.get((key[0], key[1])) == state.to_move:
        if state.board.get((key[0]-1, key[1])) == state.to_move or  state.board.get((key[0]+1, key[1])) == state.to_move:
            accumulatedValue += 5
            if state.board.get((key[0]-2, key[1])) == state.to_move or  state.board.get((key[0]+2, key[1])) == state.to_move:
                accumulatedValue += 10
                if state.board.get((key[0]-3, key[1])) == state.to_move or  state.board.get((key[0]+3, key[1])) == state.to_move:
                    accumulatedValue += 1000
    if state.board.get((key[0], key[1])) == "O":
        if state.board.get((key[0]-1, key[1])) == "O" or  state.board.get((key[0]+1, key[1])) == "O":
            accumulatedValue -= 5
            if state.board.get((key[0]-2, key[1])) == "O" or  state.board.get((key[0]+2, key[1])) == "O":
                accumulatedValue -= 10
                if state.board.get((key[0]-3, key[1])) == "O" or  state.board.get((key[0]+3, key[1])) == "O":
                    accumulatedValue -= 5000
    return accumulatedValue


def firstHeuristics(state):
    heuristicsValue = 0
    for key in state.board:
        heuristicsValue += checkVerticalConnection(state, key)
        heuristicsValue += checkHorizontalConnection(state, key)
    return heuristicsValue


