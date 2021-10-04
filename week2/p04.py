import math

time_in = input().split(':')
time_out = input().split(':')
has_cert = input() == 'Y'

minutes = (int(time_out[0]) - int(time_in[0])) * 60 + (int(time_out[1]) - int(time_in[1]))
half_hours = math.ceil(minutes / 30)
fee = half_hours * 20
if has_cert:
    fee /= 2

if has_cert and minutes < 30:
    fee = 0

print(int(fee))
