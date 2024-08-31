import pyotp

totp = pyotp.TOTP("EMAILHENNGECHALLENGE003", interval=30)
password = totp.now()
