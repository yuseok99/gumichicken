#좌표밖에 나가면 안된다
def isvaild(nx,ny):
    return 0 <=nx <11 and 0<=ny<11
#좌표에 따라 움직이는 함수
def move(x,y,dir):
    if dir == 'U':
        nx,ny = x,y+1
    elif dir == 'D':
        nx,ny = x,y-1
    elif dir == 'L':
        nx,ny = x-1,y
    elif dir =='R':
        nx,ny = x+1,y
    return nx,ny
#위함수 활용한 솔루션 함수
def solution(dirs):
    x,y =5,5
    ans = set()
    for dir in dirs:
        nx, ny = move(x,y,dir)
        if not isvaild(nx,ny):
            continue

        ans.add((x,y,nx,ny))
        ans.add((nx,ny,x,y))
        x, y = nx, ny
    return len(ans)/2

