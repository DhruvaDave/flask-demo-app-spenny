"""
    Test Credentials Example
"""

import pyotp
from common_lib.utils.password_encipherment import generate_password_hash
from common_lib.constants.constants import UTF_ENCODING
from cryptography.fernet import Fernet

PASSWORD = "Cytrio@1234"
FERNET_KEY = "k-1k6diILafCUt63-IooJplOybLy1i_hsft4gzXvt_Q\="

# Password Hash Generator
password_hash = generate_password_hash(PASSWORD)
print(f"Password: {password_hash}")

# MFA Secret Generator
mfa_secret = pyotp.random_base32()
fernet = Fernet(FERNET_KEY)
encoded_mfa_secret = fernet.encrypt(mfa_secret.encode()).decode(UTF_ENCODING)
print(f"MFA Secret: {encoded_mfa_secret}")
