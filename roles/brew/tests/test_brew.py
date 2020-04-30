def test_taps(host):
    taps = ["buo/cask-upgrade",
            "genkiroid/cert",
            "homebrew/cask",
            "homebrew/core",
            "jesseduffield/lazydocker",
            "skanehira/docui"]
    cmd = host.run("brew tap")
    for tap in taps:
        assert tap in cmd.stdout


def test_cask(host):
    casks = ["authy",
             "alfred",
             "boostnote",
             "firefox",
             "google-chrome",
             "hammerspoon",
             "macdown",
             "spectacle",
             "vagrant",
             # "virtualbox",
             "visual-studio-code",
             "showyedge",
             "grammarly",
             "slack",
             "iterm2",
             "clipy",
             "docker"]
    cmd = host.run("brew cask list")
    for cask in casks:
        assert cask in cmd.stdout


def test_packs(host):
    packs = ["cert",
             "git",
             "glib",
             "go",
             "grep",
             "httpie",
             "jq",
             "nkf",
             "oniguruma",
             "openssl",
             "peco",
             "pwgen",
             "ruby",
             "source-highlight",
             "telnet",
             "terraform",
             "tig",
             "tmux",
             "tmux-xpanes",
             "tree",
             "wget",
             "zsh",
             "zsh-completions",
             "yamllint",
             "lazydocker",
             "docui",
             "shellcheck",
             "htop",
             "ccat",
             "ffmpeg",
             "hugo",
             "nodenv"]
    cmd = host.run("brew list")
    for pack in packs:
        assert pack in cmd.stdout
