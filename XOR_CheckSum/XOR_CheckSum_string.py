def XOR_CheckSum_string(m_str, encoding="utf-8"):
    if str == type(m_str):
        m_str = bytes(m_str, encoding=encoding)
    sum = 0x0
    for c in m_str:
        sum = sum ^ c
    sum = sum ^ 0x0
    return sum
