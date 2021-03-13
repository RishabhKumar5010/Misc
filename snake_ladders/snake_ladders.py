
min_moves = -1
didit = False
moves_list = []
def quickestWayUp(ladders, snakes):
    board = list(range(100+1))
    for item in ladders+snakes:
        board[item[0]] = item[1]     
    def next6(at):
        moves = []
        normal =[]
        if at>93:return [100]
        for i in range(1,6+1):
            if (at+i)!=board[at+i]:
                moves.append(board[at+i])
            else:
                normal.append(at+i) #equivalent to board[at+i]
        if len(normal)>0:moves.append(max(normal))
        return moves
    def demorun():
        at=1
        no_moves = 0
        while at!=100 and no_moves<100:
            at = max(next6(at))
            no_moves+=1
        return no_moves
    global min_moves
    global didit
    min_moves = demorun()   # aka maximum recursion level
    didit = False
    def player_bot(at,moves_log):
        global min_moves
        global didit
        global moves_list
        if at==100:
            if len(moves_log)<=min_moves:
                min_moves = len(moves_log)
                moves_list = moves_log
            didit = True
            return 0
        if len(moves_log)>min_moves:
            return -1
        for i in next6(at):
            if i in moves_log:
                return
            else:
                player_bot(i,moves_log.copy()+[i])
    player_bot(1,[])
    return min_moves if didit else -1
        
    
                
if __name__ == '__main__':
    
    verbose = True  # change it to True for prompts at input
    
    t = int(input("No. of testcases : " if verbose else ''))

    for t_itr in range(t):
        n = int(input("No. of ladders : " if verbose else ''))

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input("Ladder : " if verbose else '').rstrip().split())))

        m = int(input("No. of snakes : " if verbose else ''))

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input("Snakes : " if verbose else '').rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        print('Min-moves :',result)
        print(' -> '.join(map(str,[1]+moves_list)))

