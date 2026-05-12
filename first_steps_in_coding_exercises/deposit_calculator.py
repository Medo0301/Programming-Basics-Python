deposit = float(input())
periot = int(input())
annual_rate = float(input()) / 100

final_amount = deposit + periot * ((deposit * annual_rate) / 12)

print(final_amount)