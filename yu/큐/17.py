def solutions(cards1, cards2, goal):
    while goal:
        if cards1[0] == goal[0] :
            cards1.pop(0)
            goal.pop(0)
        elif cards2[0] == goal[0]:
            cards2.pop(0)
            goal.pop(0)
        else:
            return "No"
    return "Yes"



print(solutions(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
