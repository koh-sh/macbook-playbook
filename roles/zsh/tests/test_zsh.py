import os


def test_shells_file(host):
    shells = host.file("/etc/shells")
    assert shells.contains("/usr/local/bin/zsh")


def test_ccat_completion(host):
    compfile = "/usr/local/share/zsh/site-functions/_ccat"
    assert host.file(compfile).is_file
