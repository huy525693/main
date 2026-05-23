import os
import sys
import urllib.request

def loadpassword():
    return os.getenv("MY_SECRET")

PASSWORD_GUARD = "HuyCoder_0706_2010_DZZ"

def ensure_keygate():
    loaded = loadpassword()
    if not loaded or loaded.strip() != PASSWORD_GUARD:
        print("Sai mật khẩu bảo vệ tool!")
        sys.exit(1)

if __name__ == "__main__":
    ensure_keygate()
    url = "https://raw.githubusercontent.com/huy525693/HUYCODERXTOOL/refs/heads/main/obf-ttc_acc_daluong.py"
    print("Đang tải và thực thi công cụ (không lưu file)...")
    try:
        with urllib.request.urlopen(url) as resp:
            code = resp.read().decode('utf-8')
        exec(code)
    except Exception as e:
        print(f"Lỗi: {e}")
        sys.exit(1)