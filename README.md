# XOR_CheckSum_zsd

这是我发布的第一个python工具，只是完成了简单的计算字符串校验和的功能\~\~\~以后再有什么还是会继续完善的\~\~\~

---------
\>\>\> from XOR_CheckSum import xor_checksum_string

\>\>\> xor_checksum_string('CCICA,0,00')

123

\>\>\> hex(xor_checksum_string('CCICA,0,00'))

'0x7b'

\>\>\> hex(xor_checksum_string('CCICA,0,00', encoding="utf-8"))

'0x7b'

\>\>\> hex(xor_checksum_string('CCICA,0,00', encoding="utf-16"))

'0x7a'

-----------

python setup.py sdist

python setup.py bdist_wheel --universal

twine upload dist/*
