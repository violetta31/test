H = 183
W = 72
S = 5000
T = 120
Rash = 0.035 * W + ((S/T)**2 / H) * 0.029 * W

print(f"Калорий сожжено: {Rash}; Пройденная дистанция: {S*(H/4+0.37)}")