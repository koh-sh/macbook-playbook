#!/bin/bash

PYTHONVER=3.9.0

export PATH="/opt/homebrew/bin:$PATH"
if command -v brew >/dev/null; then
    echo "homebrew is already installed"
else
    echo "Install homebrew"
    cd /opt || exit
    sudo mkdir homebrew 
    sudo chown -R "$(whoami)" homebrew
    curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew
fi

#if [ ! -f "$HOME/.pyenv/bin/pyenv" ]; then
#    echo "Install pyenv with version $PYTHONVER"
#    /opt/homebrew/bin/brew install pyenv
#    export PYENV_ROOT="$HOME/.pyenv"
#    export PATH="$PYENV_ROOT/bin:$PATH"
#    eval "$(pyenv init -)"
#    pyenv install "$PYTHONVER"
#    pyenv global "$PYTHONVER"
#    pip install ansible
#fi
