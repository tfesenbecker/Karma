#!/bin/bash

# -- step 2: run Palisade to create profile plots

palisade.py task zjet_excalibur plot_profiles \
    --basename-mc 'Shape_MC' \
    --basename-data 'Shape_IOV2016BCDEFGH' \
    --jec Summer16_JECV11 \
    --sample 07Aug2017 \
    --corr-levels "L1L2L3" "L1L2L3Res" "L1L2Res" \
    --quantity-pairs zpt:{jet1,jet2}pt zpt:{zmass,met,mpf,ptbalance} \
    --run-periods Run2016{BCD,EFearly,FlateGH,BCDEFGH} \
    --channel "mm" "ee" \
    --output-dir "plots" \
    --output-format 'Profiles/{jec}/{sample}/{corr_level}/{channel}/{eta}/{quantity_pair}.png'
