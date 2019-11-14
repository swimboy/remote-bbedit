# remote-bbedit
Uses iTerm2's shell integration to open remote documents in BBEdit

Process:

1) Use rsync to copy the remote file to an intermediate host that isn't behind a restrictive firewall
2) Print to the screen a bbedit command with the appropriate sftp address to open the copy on the intermediate host on the local workstation
3) Copy the command displayed on the remote terminal window and paste into a local workstation terminal window
4) Wait for the user to press a key in the remote terminal window indicating that they've finished editing the file in BBEdit
5) Use rsync to copy the file back from the intermediate server to the remote server
