# obscure64

This is a base64 based encoder/decoder tool mainly used to obscure base64 encoding to make your data transfer more secure and
interesting.

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

## Projects inspired by this library

[Emoji-Chat](https://github.com/vvanglro/Emoji-Chat)
