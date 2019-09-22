def test_extensions(host):
    extensions = ["CoenraadS.bracket-pair-colorizer-2",
                  "ms-python.python",
                  "ms-vscode.Go",
                  "shardulm94.trailing-spaces",
                  "vscode-icons-team.vscode-icons",
                  "vscoss.vscode-ansible",
                  "yzane.markdown-pdf",
                  "yzhang.markdown-all-in-one",
                  "oderwat.indent-rainbow",
                  "ms-azuretools.vscode-docker",
                  "vscodevim.vim",
                  "redhat.vscode-yaml"]
    cmd = host.run("code --list-extensions")
    for extension in extensions:
        assert extension in cmd.stdout
