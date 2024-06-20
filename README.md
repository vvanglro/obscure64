# obscure64
This is a simple base64 encoder/decoder that gives you a headache. It's just a simple wrapper around the built-in base64 module.


## Usage
```shell
pip install obscure64
```
```py
from obscure64 import Obscure64

ob64 = Obscure64()
result = ob64.encode("Hello World!".encode())
print(result)
print(ob64.decode(result))
```
And you can make it interesting.
```py
from obscure64 import Obscure64

ob64 = Obscure64(
    b64chars="🙈🙉🙊🐒🐶🐕🐩🐺🐱😹😻😼🙀😿🐈🐯🐅🐴🐎🐮🐂🐃🐄🐷🐖🐗🐽🐑🐐🐪🐘🐭🐀"
             "🐹🐰🐇🐻🐨🐼🐾🐔🐓🐣🐤🐥🐧🐸🐊🐢🐍🐲🐉🐳🐋🐬🐠🐡🐙🐚🐌🐛🐜🐝🐞🦋"
)
result = ob64.encode("Hello World!".encode())
print(result.decode())
print(ob64.decode(result))
```
