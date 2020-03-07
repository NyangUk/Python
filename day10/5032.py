al,fi,ch = map(int,input().split())

mine =al+fi
cnt=0
buy=0
while mine>=ch:
    buy = mine//ch
    mine = mine-buy*ch
    cnt =cnt+buy
    mine =mine+buy
print(cnt)