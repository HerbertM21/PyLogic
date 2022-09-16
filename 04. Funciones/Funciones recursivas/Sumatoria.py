def sumatoria (n):
    if n < 1:
        return 0
    else:
        return n + sumatoria(n - 2)

print(sumatoria(8))

# n = 8
# 8 + sumatoria(6) [8-2 = 6]
    #n = 6
    #6 + sumatoria(4)
        #n = 4
        #4 + sumatoria(2)
            #n = 2
            #2 + sumatoria(0)
                #n = 0

# n = 8
# 8 + 12 = 20
    #n = 6
    #6 + 6
        #n = 4
        #4 + 2
            #n = 2
            #2 + 0
                #n = 0