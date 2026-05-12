TRAIL_JUNIORS_FEE = 5.50
CROSS_COUNTRY_JUNIORS_FEE = 8
DOWNHILL_JUNIORS_FEE = 12.25
ROAD_JUNIORS_FEE = 20

TRAIL_SENIORS_FEE = 7
CROSS_COUNTRY_SENIORS_FEE = 9.50
DOWNHILL_SENIORS_FEE = 13.75
ROAD_SENIORS_FEE = 21.50

juniors_bikers = int(input())
seniors_bikers = int(input())
track_type = input()

donated_amount = 0

if track_type == "trail":
    donated_amount = juniors_bikers * TRAIL_JUNIORS_FEE + seniors_bikers * TRAIL_SENIORS_FEE
elif track_type == "cross-country":
    donated_amount = juniors_bikers * CROSS_COUNTRY_JUNIORS_FEE + seniors_bikers * CROSS_COUNTRY_SENIORS_FEE
    if juniors_bikers + seniors_bikers >= 50:
        donated_amount -= donated_amount * 0.25
elif track_type == "downhill":
    donated_amount = juniors_bikers * DOWNHILL_JUNIORS_FEE + seniors_bikers * DOWNHILL_SENIORS_FEE
elif track_type == "road":
    donated_amount = juniors_bikers * ROAD_JUNIORS_FEE + seniors_bikers * ROAD_SENIORS_FEE

donated_amount -= donated_amount * 0.05

print(f"{donated_amount:.2f}")