import os

input = os.path.join(os.path.dirname(__file__), "input.txt")
trees = []


for line in open(input, 'r').read().splitlines():
    trees.append(list(map(int, list(line))))

visibleTrees = [[False for tree in treerow] for treerow in trees]  # Initialize a False array
scenic_score = [[1 for tree in treerow] for treerow in trees] # Initialize a array with ones

def viewCalc(height, trees_to_check):
    view = 1
    for other_height in trees_to_check[0:-1]:
        if height > other_height:
            view += 1
        else:
            break
    return view

for x in range(0, len(trees[0])):
    for y in range(0, len(trees)):
        if (x == 0) or (x == (len(trees[0])-1)) or (y == 0) or (y == len(trees)-1):
            visibleTrees[y][x] = True
        
        height = trees[y][x]
        if not visibleTrees[y][x]:  # checking we are inside the forest
            right_trees = trees[y][(x+1):]
            left_trees = trees[y][:x]
            left_trees.reverse()
            up_trees = [row[x] for row in trees][:y]
            up_trees.reverse()
            down_trees = [row[x] for row in trees][(y+1):]

            trees_to_check = [right_trees, left_trees, up_trees, down_trees]
            scoreVal = 1
            for direction in [right_trees, left_trees, up_trees, down_trees]:
                if all(height > other_height for other_height in direction):
                    visibleTrees[y][x] = True
                if (y==3) and (x == 3):
                    pass    
                scoreVal = scoreVal*viewCalc(height, direction)
            
            scenic_score[y][x] = scoreVal

part_1 = sum(treerow.count(True) for treerow in visibleTrees)
print('Answer to part #1: '+ str(part_1))
print('Answer to part #2: '+str(max(list(map(max, *scenic_score)))))
