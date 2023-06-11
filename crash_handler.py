import os as __os
from .text import color as __color
from .text import format as __format
import secrets as __s

def crash(programName: str | None = "{programName}", err_code: int | None = 0, exception: str | None = "", reason: str | None = "No reason provided"):
    err_id = __s.token_hex(16)
    __os.system("cls")
    if exception == "":
        print(f"{__color.FAIL}{programName} has crashed!\nError ID: {err_id}\nError Code: {err_code}\n\n{reason}{__format.ENDC}")
    else:
        print(f"{__color.FAIL}{programName} has crashed!\nError ID: {err_id}\nError Code: {err_code}\nError Exception: {exception}\n\n{reason}{__format.ENDC}")
    __os.system("pause")
    exit(code=f"Crashed with: {err_code}")

def softCrash(programName: str | None = "{programName}", err_code: int | None = 0, exception: str | None = "", reason: str | None = "No reason provided", func: function | None = crash(programName="crash_handler", exception=ValueError, reason="No Function Provided")):
    err_id = __s.token_hex(16)
    __os.system("cls")
    if exception == "":
        print(f"{__color.FAIL}{programName} has soft crashed!\nError ID: {err_id}\nError Code: {err_code}\n\n{reason}{__format.ENDC}")
    else:
        print(f"{__color.FAIL}{programName} has soft crashed!\nError ID: {err_id}\nError Code: {err_code}\nError Exception: {exception}\n\n{reason}{__format.ENDC}")
    __os.system("pause")
    func()