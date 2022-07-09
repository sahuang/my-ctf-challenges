import requests
import string, random

ALLOWED_CHARS = string.ascii_letters + string.digits

FLAG = "vsctf{Buff1ng_PuBL1c_k3y_CrYpT0(Gr4phy)_15_St1LL_1n53cur3}"

def get_report_content():
    try:
        r = requests.get('https://osu.ppy.sh/users/5318910')
        if r.status_code != 200:
            return ''.join(random.choices(ALLOWED_CHARS, k=128)).encode()
        else:
            return r.content[:min(128, len(r.content))] + b"vsctf{you think flag will be in my report? Huh}"
    except:
        return ''.join(random.choices(ALLOWED_CHARS, k=128)).encode()