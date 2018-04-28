import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from XOR_CheckSum import xor_checksum_string


def test_XOR_CheckSum_string_strVSbytes():
    assert xor_checksum_string('CCICA,0,00') == xor_checksum_string(b'CCICA,0,00')


def test_XOR_CheckSum_string_bytesVSfunbytes():
    try:
        result = xor_checksum_string(bytes('CCICA,0,00', encoding="utf-8"))
    except TypeError:
        result = xor_checksum_string(bytes('CCICA,0,00'))
    assert xor_checksum_string(b'CCICA,0,00') == result


def test_XOR_CheckSum_string_content0():
    assert '0x7b' == hex(xor_checksum_string('CCICA,0,00'))


def test_XOR_CheckSum_string_content1():
    assert '0x73' == hex(xor_checksum_string('CCICI,0,00'))


def test_XOR_CheckSum_string_content2():
    assert '0x70' == hex(xor_checksum_string('CCTXA,0247718,1,1,3132333435'))


def test_XOR_CheckSum_string_encoding_utf8():
    assert '0x7b' == hex(xor_checksum_string('CCICA,0,00', encoding="utf-8"))


def test_XOR_CheckSum_string_encoding_utf16():
    assert '0x7a' == hex(xor_checksum_string('CCICA,0,00', encoding="utf-16"))


def test_XOR_CheckSum_string_encoding_gb2312():
    assert '0x7b' == hex(xor_checksum_string('CCICA,0,00', encoding="gb2312"))


if __name__ == '__main__':
    pytest.main()
