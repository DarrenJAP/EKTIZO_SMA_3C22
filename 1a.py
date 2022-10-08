def deretBilanganKali2(n):
  result = 0
  if (n > 0):
    result =  2 * deretBilanganKali2(n - 1)
    return result
  return 1

# testing
# n     = 0 1 2 3 4  5  6
# value = 1 2 4 8 16 32 64

for i in range(7):
  print(deretBilanganKali2(i))

# result
# 1
# 2
# 4
# 8
# 16
# 32
# 64