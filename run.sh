for g in $(curl -Ls https://api.chess.com/pub/player/$1/games/archives | jq -rc ".archives[]") ; do curl -Ls "$g" | jq -rc ".games[].pgn" ; done >> games.pgn
var='[Event "Live Chess"]'
sed -i "1s/.*/$var/" games.pgn
python3 -m annotator -f games.pgn -g 0.1 > processedgames.pgn
python3 processpy.py $1