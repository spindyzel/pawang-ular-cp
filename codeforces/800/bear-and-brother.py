# ░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░▄▀▀▀▄░░░░░░░░░░░░░
# ▄███▀░◐░░░▌░░░░░░░░░░░
# ░░░░▌░░░░░▐░░░░░░░░░░░░
# ░░░░▐░░░░░▐░░░░░░░░░░░░
# ░░░░▌░░░░░▐▄▄░░░░░░░░░░
# ░░░░▌░░░░▄▀▒▒▀▀▀▀▄░░░░░
# ░░░▐░░░░▐▒▒▒▒▒▒▒▒▀▀▄░░░
# ░░░▐░░░░▐▄▒▒▒▒▒▒▒▒▒▒▀▄░
# ░░░░▀▄░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄
# ░░░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀▄
# ░░░░░░░░░░░▌▌░▌▌░░░░░░░
# ░░░░░░░░░░░▌▌░▌▌░░░░░░░
# ░░░░░░░░░▄▄▌▌▄▌▌░░░░░░░
# ░░░░░░PAWANG ULAR░░░░░░
# ███████████████████████

x, y = map(int,input().split()) # input 2 varibale sekaligus
ans = 0
while(x <= y):
    x*=3; y*=2
    ans += 1
print(ans)