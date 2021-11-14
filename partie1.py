n = int(input("Un nombre qui represente la logueur et largeure du plateau(entre 3 et 27 non compris):  "))
def init_board(n):
    b = []
    for _ in range(2):                # 2 premiere rangé 2*n
        b.append([2] * n)
    for _ in range(n - 4):           # n rangé de 0*n
        b.append([0] * n)
    for _ in range(2):                # 2 derniere rangé 0*n
        b.append([1] * n)
    return b
b = init_board(n)

def print_board(b):
    l = []
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    print("  ", len(b) * " _ ", " ")         # premiere ligne de _
    for i, row in enumerate(b):
        print(len(b) - i, "⎜", '  '.join([str(n).replace("2", "B").replace("1", "W").replace("0", ".") for n in b[i]]),
              "⎜")
    print("  ", len(b) * " _ ", " ")
    for d in range(0, len(b)):
        l.append(alpha[d])
    print("   ", "  ".join(l))              # derniere ligne compose de l'alphabet
    return''
print(print_board(b))

def move(b, depart, arrivé):         # depart = (colonne, rangé)
                                     # arrivé = left ou right
    x = depart[0] - 1
    y = depart[1] - 1
    if b[y][x] == 1:
        b[y][x] = 0
        if arrivé == 'left':
            b[y-1][x-1] = 1
        elif arrivé == 'right':
            b[y-1][x+1] = 1
    elif b[y][x] == 2:
        b[y][x] = 0
        if arrivé == 'left':
            b[y+1][x+1] = 2
        elif arrivé == 'right':
            b[y+1][x-1] = 2
    return b
while not ("B" in b[-1] or "W" in b[0]):
    co = int(input("Quelle colonne?"))
    ra = int(input("Quelle rangée?"))
    direct = input("left ou right?")
    b = move(b, (co, ra), direct)
    print_board(b)