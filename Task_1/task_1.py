def hello():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")

def view():
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")
    print()
    print("  | 1 | 2 | 3 | ")
    print("  -------------")
    for i, j in enumerate(board):
        row_str = f"{i+1} | {' | '.join(j)} | "
        print(row_str)
        print("  -------------")
    print()

def move():
    while True:
        cords = input("Введите координаты хода: ").split()
        
        if len(cords) != 2:
            print("Введите 2 координаты!")
            continue
        
        x, y = cords
        
        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа!")
            continue
        
        x, y = int(x), int(y)
    
        if x < 1 or x > 3 or y < 1 or y > 3 :
            print("Некорректные координаты!")
            continue
        
        if board[x-1][y-1] != " ":
            print("Клетка занята!")
            continue
        
        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(board[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            view()
            print("Выиграл X!!!")
            return True
        if symbols == ["O", "O", "O"]:
            view()
            print("Выиграл O!!!")
            return True
    return False

hello()
board = [[" "] * 3 for i in range(3) ]
count = 0
while True:
    count += 1
    view()
    if count % 2 == 1:
        print("Ходит крестик!")
    else:
        print("Ходит нолик!")
    
    x, y = move()
    
    if count % 2 == 1:
        board[x-1][y-1] = "X"
    else:
        board[x-1][y-1] = "O"
    
    if check_win():
        break
    
    if count == 9:
        print("Поздравляем, у вас ничья")
        break
