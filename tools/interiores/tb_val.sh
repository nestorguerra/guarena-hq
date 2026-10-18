#!/bin/sh
# validate kits on seeds: tb_val.sh <kit> [kit ...] ; seeds 1..40 and 300..360 (the game's shops use that range)
cd "$(dirname "$0")/../.." || exit 1
S=$(python3 -c "print(','.join(str(i) for i in list(range(1,41))+list(range(300,361))))")
python3 tools/interiores/validar.py "$@" --semillas "$S"
