total = 0
command = input()

while command != "NoMoreMoney":
    current_sum = float(command)
    if current_sum < 0:
        print("Invalid operation!")
        break
    total += current_sum
    print(f"Increase: {current_sum:.2f}")
    command = input()
print(f"Total: {total:.2f}")
