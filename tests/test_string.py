import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from XOR_CheckSum import XOR_CheckSum_string


def test_XOR_CheckSum_string():
    assert XOR_CheckSum_string('CCICA,0,00') == XOR_CheckSum_string(b'CCICA,0,00')
    assert XOR_CheckSum_string(b'CCICA,0,00') == XOR_CheckSum_string(bytes('CCICA,0,00', encoding="utf-8"))
    assert '0x7b' == hex(XOR_CheckSum_string('CCICA,0,00'))
    assert '0x73' == hex(XOR_CheckSum_string('CCICI,0,00'))
    assert '0x70' == hex(XOR_CheckSum_string('CCTXA,0247718,1,1,3132333435'))


if __name__ == '__main__':
    pytest.main()
