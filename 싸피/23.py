cap = 2
n = 7
deliveries = [1, 0, 2, 0, 1, 0, 2]
pickups = [0, 2, 0, 1, 0, 2, 0]

distance = 0

while True:
    if [0] * len(deliveries) == deliveries:
        break
    now = 0
    index_ = 0
    for i in range(len(deliveries) - 1, -1, -1):
        if now + deliveries[i] <= cap and deliveries[i] != 0:
            if index_ == 0:
                index_ = i + 1
            now += deliveries[i]
            deliveries[i] = 0
    
    now_pickup = 0
    for i in range(index_ - 1, -1, -1):
        if now_pickup + pickups[i] <= now:
            now_pickup += pickups[i]
            pickups[i] = 0
    
    distance += index_ * 2

while True:
    if [0] * len(pickups) == pickups:
        break
    now = 0
    index_ = 0
    for i in range(len(pickups) - 1, -1, -1):
        if now + pickups[i] <= cap and deliveries[i] != 0:
            if index_ == 0:
                index_ = i + 1
            now += pickups[i]
            pickups[i] = 0
            
    distance += index_ * 2

print(distance)

# result = 16