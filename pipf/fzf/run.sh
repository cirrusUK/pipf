#!/bin/sh

python3 -m pipf.fzf.packages_list |
    fzf --multi --cycle --height 45% --preview-window right,70% \
        --preview 'python3 -m pipf.fzf.preview {1}' |
    pip install --user -U -r /dev/stdin --disable-pip-version-check --no-python-version-warning
