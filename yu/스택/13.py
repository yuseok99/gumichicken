def solution(arr,moves):
    stacks = [list(col) for col in zip(*arr)]
    stackA = []
    answer=0

    for i in moves :
        for j, val in enumerate(stacks[i-1]):
            if val != 0:
                if not stackA:  
                    stackA.append(stacks[i-1][j])
                    stacks[i-1][j] = 0
                elif stacks[i-1][j] == stackA[-1] :
                    stackA.pop(-1)
                    answer += 2

                    stacks[i-1][j] = 0
                else:
                    stackA.append(stacks[i-1][j])
                    stacks[i-1][j] = 0
                break
    return answer
    

arr = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
]

moves = [1,5,3,5,1,2,1,4]

print(solution(arr, moves))