origin= int(input(""))


interest = int(origin * 0.0375)
fee = int(interest * 0.15)
total = int(origin + interest - fee)

principal_str = format(origin, ",")
interest_str = format(interest, ",")
fee_str = format(fee, ",")
total_str = format(total,",")

fixed_width = 20

print(f"{'principal':<6} {principal_str:>{fixed_width}}")
print(f"{'interest':<6} {interest_str:>{fixed_width}}")
print(f"{'fee':<6} {fee_str:>{fixed_width}}")
print(f"{'P and I':<6} {total_str:>{fixed_width}}")
