origin= int(input(""))


interest = int(origin * 0.0375)
fee = int(interest * 0.15)
total = int(origin + interest - fee)

principal_str = format(origin, ",")
interest_str = format(interest, ",")
fee_str = format(fee, ",")
total_str = format(total,",")

left_width = 10
right_width = 15

print(f"{'principal':<{left_width}} {principal_str:>{right_width}}")
print(f"{'interest':<{left_width}} {interest_str:>{right_width}}")
print(f"{'fee':<{left_width}} {fee_str:>{right_width}}")
print(f"{'P and I':<{left_width}} {total_str:>{right_width}}")
