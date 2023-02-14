import sys
import chess.pgn as pgnner
import chess.pgn

f = open("processedgames.pgn")

acpls = []

headers = []

while True:
    game = chess.pgn.read_headers(f)
    if game is None:
        break  # end of file

    headers.append(game)

for header in headers:
    if header["White"] == sys.argv[1]:
        acpls.append(int(header["WhiteACPL"]))

    else:
        acpls.append(int(header["BlackACPL"]))

# plotting
print(acpls)
import matplotlib.pyplot as plt
plt.hist(acpls, bins=30)
plt.show()