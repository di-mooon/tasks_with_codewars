def multiplyAll(lst):
    def m_a(n):
        return [x*n for x in lst]
    return m_a

print(multiplyAll([1,2,3])(3))