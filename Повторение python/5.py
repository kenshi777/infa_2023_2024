def second_max(N):
    m_1 = N[0]
    m_2 = N[1]
    for i in range(2, len(N)):
        if N[i] > m_1:
            m_2 = m_1
            m_1 = N[i]
        elif N[i] > m_2 and N[i] != m_1:
            m_2 = N[i]
    return m_2 

print(second_max([1, 7, 4, 6, 2, 12, 10, 6, 4])) 