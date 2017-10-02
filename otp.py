#!/usr/bin/python3

ch = [bytearray.fromhex("BB3A65F6F0034FA957F6A767699CE7FABA855AFB4F2B520AEAD612944A801E"),
      bytearray.fromhex("BA7F24F2A35357A05CB8A16762C5A6AAAC924AE6447F0608A3D11388569A1E"),
      bytearray.fromhex("A67261BBB30651BA5CF6BA297ED0E7B4E9894AA95E300247F0C0028F409A1E"),
      bytearray.fromhex("A57261F5F0004BA74CF4AA2979D9A6B7AC854DA95E305203EC8515954C9D0F"),
      bytearray.fromhex("BB3A70F3B91D48E84DF0AB702ECFEEB5BC8C5DA94C301E0BECD241954C831E"),
      bytearray.fromhex("A6726DE8F01A50E849EDBC6C7C9CF2B2A88E19FD423E0647ECCB04DD4C9D1E"),
      bytearray.fromhex("BC7570BBBF1D46E85AF9AA6C7A9CEFA9E9825CFD5E3A0047F7CD009305A71E")]

keyFull = bytearray.fromhex("00000000000000000000000000000000000000000000000000000000000000")


def findKeyPart(position, chr, array1, array2):
  for key in range(0, 256):
    if (key ^ array1[position] == 32 and key ^ array2[position] == chr) or (
                        key ^ array2[position] == 32 and key ^ array1[position] == chr):
      if isValidKey(key, position):
        keyFull[position] = key


def isValidKey(key, position):
  for list in ch:
    if position >= len(list):
      continue
    if ((list[position] ^ key) < 65 and (list[position] ^ key) != 32) or (list[position] ^ key) > 122:
      return False
  return True


def decryptMessage():
  for cipher in ch:
    for x in range(0, len(cipher)):
      print(chr(cipher[x] ^ keyFull[x]), end="")
    print()


def findSub(list, pos, char):
  for z in range(0, 256):
    if ch[list][pos] ^ z == ord(char):
      return z
  return 0


for j in range(0, len(ch)):
  for k in range(0, len(ch)):
    if j == k:
      continue
    smallest = 0
    if len(ch[j]) <= len(ch[k]):
      smallest = len(ch[j])
    else:
      smallest = len(ch[k])
    for x in range(0, smallest):
      z = ch[j][x] ^ ch[k][x]
      if z >= 64:
        for y in range(0, 127):
          if 32 ^ y == z:
            findKeyPart(x, y, ch[j], ch[k])

keyFull[-1] = findSub(0, -1, ".")
keyFull[-2] = findSub(0, -2, "n")
keyFull[-11] = findSub(0, -11, "e")
keyFull[0] = findSub(2, 0, "T")
keyFull[6] = findSub(4, 6, "k")
keyFull[8] = findSub(0, 8, "n")
keyFull[10] = findSub(0, 10, "i")
keyFull[17] = findSub(4, 17, "l")

decryptMessage()
print(keyFull)
