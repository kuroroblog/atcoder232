# 標準入力を受け付ける。
s = input()
t = input()

# Sの各文字をK個後ろの英小文字に変更する関数を作成する。
# 参考 : https://qiita.com/TodayInsane/items/94f495db5ba143a8d3e0
def rot_n(s, n):
    answer = ''
    for letter in s:
        answer += chr(ord('a') + (ord(letter) - ord('a') + n) % 26)

    return answer

# 0から始めるのは、文字列Sを変更しない場合も考慮するため。
for k in range(0, 26):
    if rot_n(s, k) == t:
        print('Yes')
        exit()

print('No')
