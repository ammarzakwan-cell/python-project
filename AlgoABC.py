plain = "fscyberx2020"

def a(inp):
  tmp = [0] * len(inp)
  for i in range(len(inp)):
    tmp[i] = inp[len(inp)-1-i]
  inp = tmp
  b(inp)


def b(inp):
  for i in range(len(inp)):
    if (i % 2 == 0):
      inp[i] = ord(inp[i]) + i
    else:
      inp[i] = ord(inp[i]) + i
  c(inp)


def c(inp):
  for i in range(len(inp)):
    if (inp[i] > 100):
      inp[i] = inp[i] - 100
      inp[i] = inp[i] ^ 0x09
    else:
      inp[i] = inp[i] + 100
      inp[i] = inp[i] ^ 0x05
  check(inp)


def check(inp):
  enc = [29, 6, 10, 8, 16, 13, 168, 168, 168, 17, 170, 3, 31, 179, 45, 189, 22, 26]
  if (enc == inp):
    print("Win")
  else:
    print("Lose")


if (len(plain) != 18):
  print("Bye")
else:
  a(plain)
