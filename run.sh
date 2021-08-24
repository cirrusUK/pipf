#!/bin/sh

python3 -m pipi.fzf.packages_list |
    fzf --multi --cycle --height 45% --preview-window right,70% \
        --preview 'python3 -m pipi.fzf.preview {1}'
