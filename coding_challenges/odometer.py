# Odometer has n slots. Write code to make it roll.


def increment_odometer(slots:list[int])->list[int]:
    for i in reversed(range(0, len(slots))):
        # increment first slot
        if i == len(slots)-1:
            slots[i] += 1

        # handle carries
        if slots[i]==10:
            slots[i]=0
            if i >= 1:
                slots[i-1] +=1
    return slots


print(increment_odometer([1]))
print(increment_odometer([1,2]))
print(increment_odometer([9,9]))
print(increment_odometer([1,9]))
