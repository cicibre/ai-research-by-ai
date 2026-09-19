#!/usr/bin/env bash
# fetch_connectomes.sh — download the connectome data this programme analysed, from its source.
#
# WHY THIS SCRIPT EXISTS INSTEAD OF THE DATA.
# The data was committed into a PUBLIC mirror on 2026-09-19 on a false premise: that it was
# "already publicly distributed" via cicibre/academics. Academics is PRIVATE, so that copy was a
# FIRST PUBLICATION of third-party data rather than a mirror — and the licence is UNDETERMINED
# (Netzschleuder states no dataset licence for celegans_2019; the AGPL-v3 in its footer governs
# the site's software). Redistribution was asserted, not checked. The data was therefore removed
# and replaced with this, which keeps every result reproducible WITHOUT redistributing anything.
#
# THE DATA IS NOT OURS. Cite the original authors, never this repository.
#
#   Cook, S.J. et al. (2019), "Whole-animal connectomes of both Caenorhabditis elegans sexes,"
#   Nature 571:63-71.  https://doi.org/10.1038/s41586-019-1352-7
#   Obtained via Netzschleuder, dataset `celegans_2019`; canonical at wormwiring.org.
#   Drosophila larval whole-brain: Netzschleuder dataset `fly_larva`.
#
# USAGE:  bash fetch_connectomes.sh          (run from anywhere; writes beside itself)
# EXIT :  0 = every file present and checksum-verified · 1 = a download or checksum failed
#
# ⚠️ CHECKSUMS ARE PINNED TO THE EXACT BYTES THE PUBLISHED RESULTS WERE COMPUTED FROM.
# If upstream changes the data, this script FAILS LOUDLY rather than silently analysing something
# else. A mismatch is not a reason to delete the check — it is the finding.
set -u
cd "$(dirname "$0")" || exit 1

BASE_CE="https://networks.skewed.de/net/celegans_2019/files"
BASE_FL="https://networks.skewed.de/net/fly_larva/files"

# name|url|sha256-of-the-zip-the-results-used
SETS=(
"hermaphrodite_chemical_corrected|$BASE_CE/hermaphrodite_chemical_corrected.csv.zip|0f6636a92f8c4acbcff46c17b9144b8afdfad7c169008e04b9a64e209b7d1429"
"hermaphrodite_gap_junction_corrected|$BASE_CE/hermaphrodite_gap_junction_corrected.csv.zip|66474f849fcb6cb2cd931d4255f74b0c59a007a857821fa0aee1730d2ed02f77"
"male_chemical_corrected|$BASE_CE/male_chemical_corrected.csv.zip|5c98d115d2b575c98ea60dfa55add2ade4cddbd1347e67be92210543f3b7693f"
"male_gap_junction_corrected|$BASE_CE/male_gap_junction_corrected.csv.zip|2443e52b7bc1c8846d6e21075e4d93259e3e48ba2af3d2812e7e2c01a2d74357"
"fly_larva|$BASE_FL/fly_larva.csv.zip|6a8b7d8f2287027fba6723e1db41df968b4668469072b6ee4af314a2eabd1edc"
)

sha() { shasum -a 256 "$1" 2>/dev/null | cut -d' ' -f1 || sha256sum "$1" | cut -d' ' -f1; }

rc=0
echo "── fetching connectome data from source ──"
for row in "${SETS[@]}"; do
  name="${row%%|*}"; rest="${row#*|}"; url="${rest%%|*}"; want="${rest##*|}"
  zip="${name}.csv.zip"

  if [ -f "$zip" ] && [ "$(sha "$zip")" = "$want" ]; then
    echo "  ✓ $name  (already present, checksum matches)"
  else
    echo "  ↓ $name"
    if ! curl -fsSL --max-time 300 -o "$zip.part" "$url"; then
      echo "    ⛔ DOWNLOAD FAILED: $url"; rc=1; continue
    fi
    got=$(sha "$zip.part")
    if [ "$got" != "$want" ]; then
      echo "    ⛔ CHECKSUM MISMATCH — upstream data has changed."
      echo "       expected $want"
      echo "       got      $got"
      echo "       THIS IS A FINDING, NOT A NUISANCE: the published results were computed from the"
      echo "       expected bytes. Do not delete this check. Record the change and re-derive."
      rm -f "$zip.part"; rc=1; continue
    fi
    mv "$zip.part" "$zip"
  fi

  # extract to the layout the harnesses expect: <name>/{nodes,edges,gprops}.csv
  if [ ! -f "$name/nodes.csv" ] || [ ! -f "$name/edges.csv" ]; then
    mkdir -p "$name"
    if ! unzip -oq "$zip" -d "$name" 2>/dev/null; then
      echo "    ⛔ UNZIP FAILED for $zip"; rc=1; continue
    fi
    # some archives nest one directory deep; flatten if so
    if [ ! -f "$name/nodes.csv" ]; then
      inner=$(find "$name" -name nodes.csv -maxdepth 3 | head -1)
      [ -n "$inner" ] && mv "$(dirname "$inner")"/*.csv "$name/" 2>/dev/null
    fi
  fi
  [ -f "$name/nodes.csv" ] && [ -f "$name/edges.csv" ] \
    && echo "    → $name/{nodes,edges}.csv" \
    || { echo "    ⛔ expected files missing after extraction"; rc=1; }
done

echo
if [ "$rc" = 0 ]; then
  echo "  ALL SETS PRESENT AND VERIFIED against the bytes the published results used."
  echo "  The C. elegans harness additionally asserts n == 300 neurons and refuses to run otherwise;"
  echo "  that is an independent check on the extraction, not a substitute for these checksums."
else
  echo "  ⛔ INCOMPLETE — see above. Results cannot be reproduced until this exits 0."
fi
exit "$rc"
