# Google Authenticator One Time Password

## Overview

This small script creates a TOTP secret, writes a provisioning URI to (`totp.config`) and a QR image to (`totp_qr_code.png`), and can read the saved provisioning URI to generate current OTPs.

## Requirements

- Python 3.8+
- Packages: `pyotp`, `qrcode`, `Pillow`

Install dependencies:

```powershell
python -m pip install pyotp qrcode pillow
```

## Usage

- Generate a new secret and QR image (also saves the provisioning URI to `totp.config`):

```powershell
python main.py -generate-qr
```

Scan `totp_qr_code.png` with Google Authenticator (or similar) to add the account.

- Display current OTPs using the secret key from the generated provisioning URI saved in `totp.config`:

```powershell
python main.py -get-otp
```


