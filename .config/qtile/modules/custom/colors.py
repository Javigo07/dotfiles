import os

colors = []
colors1 = []

cache='/home/javigo07/.config/wal/walcache/colors'

def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(16):
            if i != 0 and i <= 9:
                colors1.append(file.readline().strip())
            colors.append(file.readline().strip())
load_colors(cache)

#print(colors, "and", colors1)


