# remote-bbedit
This python script and shell function use iTerm2's API to open remote documents in BBEdit

# How It Works #

The shell function provides a command on the remote host named `bbedit` that copies the referenced file via SFTP to an intermediate server that is reachable by both the local and remote hosts. It then sends a control sequence that iTerm detects and launches the python script on the local host that opens the referenced file via SFTP on the intermediate host. When the file is saved and closed, the remote host then copies the file back to its original location, deleting the copy on the remote host.