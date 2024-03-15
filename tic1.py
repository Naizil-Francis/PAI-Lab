n = 3
count = 0
mat = [['*'] * n for _ in range(n)]

def print_matrix():
    for row in mat:
        print(" ".join(row))

def condition():
    while True:
        x, y = map(int, input("Enter the row and col indices (space-separated): ").split())
        if mat[x][y] == '*':
            break
        else:
            print("Invalid Index. Try again!!")
    return x, y

def check_winner(player):
    for i in range(n):
        if all(mat[i][j] == player for j in range(n)) or all(mat[j][i] == player for j in range(n)):
            return True
    return all(mat[i][i] == player for i in range(n)) or all(mat[i][n - i - 1] == player for i in range(n))

def game(player, count):
    count += 1
    if count > 9:
        print("Tie Game")
        exit(0)
    print(f'\nPlayer {player}')
    x, y = condition()
    mat[x][y] = player
    print_matrix()
    if check_winner(player):
        print(f"Player {player} won the game")
        exit(0)
    return count

while True:
    count = game('X', count)
    count = game('O', count)