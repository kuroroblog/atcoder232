import itertools

# 標準入力を受け付ける。
N, M = map(int, input().split())

takahashi_list = []
for _ in range(M):
    A, B = map(int, input().split())
    takahashi_list.append([A, B])

aoki_list = set(())
for _ in range(M):
    C, D = map(int, input().split())
    # ボールの順序が逆になるパターンも考慮する。
    aoki_list.add((C, D))
    aoki_list.add((D, C))

# 全列挙するための準備
num_list = []
for i in range(1, N + 1):
    num_list.append(i)

# itertools.permutations参考 : https://minus9d.hatenablog.com/entry/2017/04/30/110855
for v in itertools.permutations(num_list, N):
    cnt = 0
    for k in range(M):
        ball_i, ball_j = takahashi_list[k]
        if (v[ball_i - 1], v[ball_j - 1]) in aoki_list:
            cnt += 1

    if cnt == M:
        print('Yes')
        exit()
print('No')
