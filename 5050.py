import random

head = 'HEAD'
tail = 'TAIL'
coins = [head, tail]

for i in range(1):
    coin = random.choice(coins)
    print(f"La pièce a été jouée et se trouve être : {coin}")

 # Pour plus que 1 : print(f"Les pièces ayant été jouées sont : {coins}")