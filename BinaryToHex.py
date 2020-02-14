# Alex London
# 02/14/20
# COSC 221 - Computer Organization
# Program reads binary from a file, removes spaces and then converts to hex.
# Hex is formatted then written to a different file.

# open/create files
binaryFile = open("binary.txt", "r")
binaryFile = binaryFile.readlines()
hexFile = open("hex.txt", "a+")

# loop through each line of binaryFile then convert and write to hexFile
for line in binaryFile:
    binaryCode = line.replace(" ", "")
    hexCode = hex(int(binaryCode, 2))
    hexCode = hexCode.replace("0x", "").upper().zfill(4)
    hexFile.write(hexCode + "\n")

# close hexFile
hexFile.close()
