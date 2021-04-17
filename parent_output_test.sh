#!/bin/bash

set -euo pipefail

output="$1"
got=$(cat "../../$output")
want="important text"


if [[ $got != "$want" ]]; then
  echo "'$got'" >&2
  printf "error: program output does not contain: \n'%s'" "$want" >&2
  exit 1
fi
