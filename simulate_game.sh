#!/bin/bash

GAME_SCRIPT="main.py"

if [[ ! -f "$GAME_SCRIPT" ]]; then
  echo "Error: Tic-Tac-Toe script not found at $GAME_SCRIPT"
  exit 1
fi

simulate_random_moves() {
  for ((i=0; i<9; i++)); do
    sleep 0.5
    echo $(( RANDOM % 9 ))
  done
}

simulate_random_moves | python3 "$GAME_SCRIPT"
