def test_sudoers(host):
    iam = host.user().name
    content = "(ALL) NOPASSWD: ALL"
    with host.sudo():
        output = host.run("sudo -lU " + iam)
        assert output.stdout.find(content) != -1
