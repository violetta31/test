Height = 168
Weight = 59
Steps = 5000
Time = 120
Rash = 0.035 * Weight + ((Steps/Time)**2 / Height) * 0.029 * Weight

print(f"Калорий сожжено: {Rash}; Пройденная дистанция: {Steps*(Height/4+0.37)}")