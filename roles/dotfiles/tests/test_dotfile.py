import os


def test_dotfiles(host):
    homedir = os.environ["HOME"] + "/"
    files = [".tigrc",
             ".tmux.conf",
             ".vimrc",
             ".zshrc",
             ".hammerspoon/init.lua"]
    for file in files:
        dotfile = host.file(homedir + file)
        assert dotfile.is_file
