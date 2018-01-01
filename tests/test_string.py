import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from XOR_CheckSum import XOR_CheckSum_string


def test_XOR_CheckSum_string_strVSbytes():
    assert XOR_CheckSum_string('CCICA,0,00') == XOR_CheckSum_string(b'CCICA,0,00')


def test_XOR_CheckSum_string_bytesVSfunbytes():
    assert XOR_CheckSum_string(b'CCICA,0,00') == XOR_CheckSum_string(bytes('CCICA,0,00', encoding="utf-8"))


def test_XOR_CheckSum_string_content0():
    assert '0x7b' == hex(XOR_CheckSum_string('CCICA,0,00'))


def test_XOR_CheckSum_string_content1():
    assert '0x73' == hex(XOR_CheckSum_string('CCICI,0,00'))


def test_XOR_CheckSum_string_content2():
    assert '0x70' == hex(XOR_CheckSum_string('CCTXA,0247718,1,1,3132333435'))


def test_XOR_CheckSum_string_encoding_utf8():
    assert '0x7b' == hex(XOR_CheckSum_string('CCICA,0,00', encoding="utf-8"))


def test_XOR_CheckSum_string_encoding_utf16():
    assert '0x7a' == hex(XOR_CheckSum_string('CCICA,0,00', encoding="utf-16"))


if __name__ == '__main__':
    pytest.main()
