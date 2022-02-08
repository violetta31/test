Height = 168
Weight = 59
Steps = 4000
Time = 160
callories = 0.035 * Weight + ((Steps/Time)**2 / Height) * 0.029 * Weight
distance = Steps*(Height/4+0.37)/1000
print(f"Калорий сожжено: {callories}; Пройденная дистанция: {distance}")
if (distance < 2):
    print("Ходите больше!")
elif (distance > 2 and distance < 4):
    print("Ещё чуть-чуть!")
else :
    print("Молодец!")