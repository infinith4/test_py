import pyotp
import time

print('test')

totp = pyotp.TOTP('base32secret3232')
totp_val = totp.now() # => '492039'
print(f'totp_val: {totp_val}')

# OTP verified for current time
veryfy = totp.verify(totp_val) # => True
print(f'veryfy: {veryfy}')
time.sleep(30)
veryfy = totp.verify('492039') # => False
print(f'veryfy: {veryfy}')
