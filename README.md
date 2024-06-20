# obscure64
[![Package version](https://img.shields.io/pypi/v/obscure64?color=%2334D058&label=pypi%20package)](https://pypi.python.org/pypi/obscure64)

This is a base64 based encoder/decoder tool mainly used to obscure base64 encoding to make your data transfer more secure and
interesting.

## Usage

```shell
pip install obscure64
```
Obfuscated coded data, causing headaches for those who get it.🤕
```py
from obscure64 import Obscure64

ob64 = Obscure64()
result = ob64.encode("Hello World!".encode())
print(result)  # output: b'sgvSBg8Gv29YBgqH'
print(ob64.decode(result))  # output: b'Hello World!'

import base64
print(base64.b64encode("Hello World!".encode()))  # output: b'SGVsbG8gV29ybGQh'
```

And you can make it interesting.🤔

```py
from obscure64 import Obscure64

ob64 = Obscure64(
    b64chars="🙈🙉🙊🐒🐶🐕🐩🐺🐱😹😻😼🙀😿🐈🐯🐅🐴🐎🐮🐂🐃🐄🐷🐖🐗🐽🐑🐐🐪🐘🐭🐀"
             "🐹🐰🐇🐻🐨🐼🐾🐔🐓🐣🐤🐥🐧🐸🐊🐢🐍🐲🐉🐳🐋🐬🐠🐡🐙🐚🐌🐛🐜🐝🐞🦋"
)
result = ob64.encode("Hello World!".encode())
print(result.decode())  # output: 🐎🐩🐃🐥🐑🐩🐛🐀🐃🐬🐜🐲🐑🐩🐅🐹
print(ob64.decode(result))  # output: b'Hello World!'
```

## Projects inspired by this library

[Emoji-Chat](https://github.com/vvanglro/Emoji-Chat)
