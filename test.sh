#!/bin/bash

die() {
  echo "$*"
  exit 1
}

[[ -x ./minesweeper.pl ]] || die "Could not find ./minesweeper.pl"
[[ -f acceptance.txt ]] || die "Could not find ./acceptance.txt"
[[ -f solution.txt ]] || echo "Creating solution.txt"
[[ -f solution.txt ]] || ./minesweeper.pl <acceptance.txt > solution.txt || die "Conld not generate solution.txt"

./minesweeper.pl <acceptance.txt | cmp - solution.txt || die "Test failed"
