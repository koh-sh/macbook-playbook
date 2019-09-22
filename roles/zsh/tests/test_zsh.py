def test_shells_file(host):
    shells = host.file("/etc/shells")
    assert shells.contains("/usr/local/bin/zsh")
