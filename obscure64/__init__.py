from __future__ import annotations
import base64
import string
from importlib.metadata import version

__version__ = version("obscure64")
__all__ = [
    "__version__",
    "Obscure64"
]


class Obscure64:

    def __init__(self, b64chars: str | None = None):
        """
        :param b64chars: 65 characters long string.
        """
        if not b64chars:
            b64chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + "+/="
        self.b64chars = b64chars
        self._std_b64chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/="
        if len(self._std_b64chars) != len(set(self.b64chars)):
            raise ValueError("b64chars must be 65 characters long and not repeated.")
        self._encode_map = str.maketrans(self._std_b64chars, self.b64chars)
        self._decode_map = str.maketrans(self.b64chars, self._std_b64chars)

    def encode(self, text: bytes) -> bytes:
        base64_text = base64.b64encode(text).decode('utf-8')
        encrypted_text = base64_text.translate(self._encode_map)
        return encrypted_text.encode('utf-8')

    def decode(self, text: str | bytes) -> bytes:
        if isinstance(text, bytes):
            text = text.decode('utf-8')
        standard_base64_text = text.translate(self._decode_map)
        return base64.b64decode(standard_base64_text)
