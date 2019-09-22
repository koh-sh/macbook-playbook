def test_docker_completion(host):
    commands = ["docker", "docker-compose", "docker-machine"]
    srcpath = "/Applications/Docker.app/Contents/Resources/etc/"
    dstpath = "/usr/local/share/zsh/site-functions/"
    for cmd in commands:
        symlink = host.file(dstpath + "_" + cmd)
        assert symlink.linked_to == srcpath + cmd + ".zsh-completion"
