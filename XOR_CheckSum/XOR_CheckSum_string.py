def xor_checksum_string(m_str, encoding="utf-8"):
    if str == type(m_str):
        try:
            m_str = bytes(m_str, encoding=encoding)
        except:
            m_str = m_str.encode(encoding=encoding)
    XOR_sum = 0x0
    for c in m_str:
        try:
            XOR_sum = XOR_sum ^ c
        except:
            XOR_sum = XOR_sum ^ ord(c)
    XOR_sum = XOR_sum ^ 0x0
    return XOR_sum
