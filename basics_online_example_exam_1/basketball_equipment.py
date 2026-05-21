basketball_yearly_fee = int(input())

shoes_price = basketball_yearly_fee - (basketball_yearly_fee * 0.40)
uniform_price = shoes_price - (shoes_price * 0.20)
ball_price = uniform_price / 4
accessories_price = ball_price / 5

final_price = basketball_yearly_fee + shoes_price + uniform_price + ball_price + accessories_price

print(f"{final_price:.2f}")