import pyotp
import qrcode
import sys
from pathlib import Path


def generate_secret_key() -> str:
    return pyotp.random_base32()

def generate_qr_code(data: str) -> None:
    img = qrcode.make(data)
    img.save("totp_qr_code.png")
    Path("totp.config").write_text(data)

def generate_totp_code(secret_key: str) -> str:
    totp = pyotp.TOTP(secret_key)
    return totp.now()

# Example TOTP Key: otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example

def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "-generate-qr":
        secret_key: str = generate_secret_key()
        email: str = "adam.smashem@arasaka.co.jp"
        issuer: str = "Arasaka"
        totp_uri: str = pyotp.totp.TOTP(secret_key).provisioning_uri(name=email, issuer_name=issuer)
        generate_qr_code(totp_uri)
        print("QR code and provisioning URI saved")
    elif len(sys.argv) > 1 and sys.argv[1] == "-get-otp":
        config_path = Path("totp.config")
        if not config_path.exists():
            print("totp.config is does not exist. Use -generate-qr to generate a totp uri.")
            return
        totp_uri_contents = config_path.read_text().strip()
        if not totp_uri_contents:
            print("totp.config is empty. Use -generate-qr to generate a totp uri.")
            return
        try:
            secret_key = totp_uri_contents.split("secret=")[1].split("&")[0]
        except Exception:
            print("failed to parse secret from totp.config")
            return

        while True:
            totp_code: str = generate_totp_code(secret_key)
            print(f"Current TOTP Code: {totp_code}")
            input("Press Enter to refresh the code or Ctrl + C to exit...")
    else:
        print("  python main.py -generate-qr")
        print("  python main.py -get-otp")



if __name__ == "__main__":
    main()