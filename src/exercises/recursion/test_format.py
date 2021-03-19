def diamond_ite(levels: int) -> None:
    """Print a diamond"""
    duoStarNum= 2 * levels - 1
    duoLevels = 2 * levels - 1
    while duoStarNum > 1:
        print('{:{align}{width}}'.format('*'*duoStarNum, align='^', width=(duoLevels)))
        duoStarNum -= 2 
    while duoStarNum <= duoLevels:
        print('{:{align}{width}}'.format('*'*duoStarNum, align='^', width=(duoLevels)))
        duoStarNum += 2
diamond_ite(5)