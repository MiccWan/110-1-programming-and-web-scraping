def step(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


def draw(g, from_x, from_y, to_x, to_y):
    step_x = step(to_x - from_x)
    step_y = step(to_y - from_y)
    cur_x = from_x
    cur_y = from_y

    while cur_x != to_x or cur_y != to_y:
        g[cur_y][cur_x] = '＊'
        cur_x += step_x
        cur_y += step_y
    
    g[cur_y][cur_x] = '＊'


def render(g):
    for line in reversed(g):
        print(''.join(line))

n, m, p = map(int, input().split(' '))
graph = [['Ｏ' for i in range(m)] for j in range(n)]
new_x, new_y = map(int, input().split(' '))
for i in range(p - 1):
    last_x, last_y = new_x, new_y
    new_x, new_y = map(int, input().split(' '))
    draw(graph, last_x, last_y, new_x, new_y)

render(graph)
