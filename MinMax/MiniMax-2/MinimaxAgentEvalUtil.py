import util
def minimaxAgentEval(gameState):
    pos = gameState.getPacmanPosition()
    food = gameState.getFood()
    ghostStates = gameState.getGhostStates()

    if gameState.isWin():
        return float("inf")

    for ghostState in ghostStates:
        if util.manhattanDistance(ghostState.getPosition(), pos) < 2 and ghostState.scaredTimer < 3:
            return float("-inf")

    foodDist = []
    for food in list(food.asList()):
        foodDist.append(util.manhattanDistance(food, pos))

    return gameState.getScore() - 5 * min(foodDist)
