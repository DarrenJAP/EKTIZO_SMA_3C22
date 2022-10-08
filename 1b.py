def deretAngka(n, max=0, reverse=False):
  if max == 0:
    max = n

  if n > 0 and not reverse:
    print(n)
    deretAngka(n-1, max)
  elif n == 0 or reverse:
    if n < max:
      print(n+1)
      deretAngka(n+1, max, True)

# testing

deretAngka(5)
print("\n")
deretAngka(10)

# result
# 5
# 4
# 3
# 2
# 1
# 1
# 2
# 3
# 4
# 5


# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10