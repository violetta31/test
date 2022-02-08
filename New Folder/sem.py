Height = 168
Weight = 59
Steps = 4000
Time = 160
Rash = 0.035 * Weight + ((Steps/Time)**2 / Height) * 0.029 * Weight
Distance = Steps*(Height/4+0.37)/1000
print(f"Калорий сожжено: {Rash}; Пройденная дистанция: {Distance}")