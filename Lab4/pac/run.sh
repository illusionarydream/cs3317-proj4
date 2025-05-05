python pacman.py \
  -p ExpectimaxAgent \
  -g RandomGhost \
  -l testClassic \
  -a depth=4 \
  -n 100 \
  -q

python pacman.py \
  -p ExpectimaxAgent \
  -g MinimaxGhost \
  -l testClassic \
  -a depth=4 \
  -n 100 \
  -q

python pacman.py \
  -p MinimaxAgent \
  -g RandomGhost \
  -l testClassic \
  -a depth=4 \
  -n 100 \
  -q

python pacman.py \
    -p MinimaxAgent \
    -g MinimaxGhost \
    -l testClassic \
    -a depth=4 \
    -n 100 \
    -q