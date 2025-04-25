coins = [20,10,5,1,.5, .25, .10, .05, .01]

def make_change(price:float, cash:float)->dict[float,int]:
    # handle edge cases
    if price == 0 and cash == 0:
        return {}
    if round(cash - price,2) == 0:
        return {}
    if cash < price:
        raise Exception("Customer didn't give enough money.")
    # Let's try floats first. May need to switch to decimal.
    change = {}
    # Probably will need to stress test to see if any rounding situations don't match business rules or intuition.
    # Or switch to decimal type.
    remainder = round(cash - price,2)
    print(f"We owe the customer {remainder}")
    for coin in coins:
        print(f"Checking {coin}")
        difference= round(remainder - coin,2)
        print(difference, coin)
        if difference <1:
            print("Too big")
            continue
        if difference>=0:
            print("Just right")
            if coin in change:
                change[coin] +=1
            else:
                change[coin] = 1
            remainder = difference - coin
        else:
            return change
    if change:
        return change

    # Alternately remove the guards at top and return {}
    raise Exception("Shouldn't get here")
    # Degenerate case?
    return {}


if __name__ == '__main__':
    # edge cases
    assert make_change(0, 0) == {}
    assert make_change(100,100) == {}
    # simple case
    result =make_change(99.99, 100)
    assert result == {0.01:1},result
    # complex case
    assert make_change(99.92, 100) == {0.01:3,0.05:1}
