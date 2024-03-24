
import zugbruecke as ctypes
import zugbruecke.wintypes as wintypes

class HomeTaxEncrypt(object):
    def __init__(self):
        self.fcrypt_es = ctypes.windll.LoadLibrary('./fcrypt_es.dll')
        self.encrypt_file = self.fcrypt_es.DSFC_EncryptFile
        self.encrypt_file.argtypes = (
            wintypes.HWND,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
            wintypes.UINT,
        )

    def encryptFile(self, originalPath, encryptFilePath, password):
        print('encryptFile')
        print(repr(originalPath).encode())
        print(repr(encryptFilePath).encode())
        print(repr(password).encode())
        result = self.encrypt_file(0, originalPath.encode(), encryptFilePath.encode(), str(password).encode(), 1)
        print(result)
        return result
