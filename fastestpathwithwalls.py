def solution(arr, walls):
    if arr[0][0] == 1:
        return -1
    height = len(arr)
    width = len(arr[0])
    # Create a matrix of size height*width that we can use to track visits
    visited = [[-1]*width for i in range(height)]
    visited[0][0] = 1
    # Queue element format is [x,y,distance,how many walls it can remove]
    queue = [[0,0,1,walls]]
    # BFS of matrix
    while len(queue) > 0:
        el = queue.pop(0)
        x, y, distance, walls = el[0], el[1], el[2], el[3]
        movement = [[x+1,y],[x,y+1],[x-1,y],[x,y-1],[x+1,y+1], [x+1,y-1], [x-1,y-1], [x-1,y+1]]
        for move in movement:
            newX = move[0]
            newY = move[1]
            if (newX>=width or newY>=height or newX<0 or newY<0):
                continue
            elif (arr[newY][newX]==1 and walls==0) or visited[newY][newX]>=walls:
                continue
            elif(newY == height-1 and newX == width-1):
                return distance+1
            else:
                visited[newY][newX] = walls
                queue.append([newX, newY, distance+1, walls-arr[newY][newX]])
    return -1
