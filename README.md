# remote-bbedit
This python script and shell function use iTerm2's API to open remote documents in BBEdit running on the local host. Other solutions for this exist, but run into problems when a restrictive firewall is in the way, or if the root user is barred from logging in remotely.

This solution will work as long as the local and remote users have SSH access to an intermediate server where the file to be edited is stored temporarily.

---

## How It Works ##

The shell function provides a command on the remote host named `bbedit` that copies the referenced file via SFTP to an intermediate server that is reachable by both the local and remote hosts. It then sends a control sequence that iTerm detects and launches the python script on the local host that opens the referenced file via SFTP on the intermediate host. When the file is saved and closed, the remote host then copies the file back to its original location, deleting the copy on the intermediate host.

## How to Install ##

1. Make sure that you have the BBEdit command line tools and the iTerm2 python runtime installed.

2. Make sure that both the local and remote host can SSH to the intermediate server without user intervention. If you use `sudo` you'll need to make sure that the root user can also connect. The goal is to be able to connect with `ssh synchost` without any parameters and without entering a password. The most common method to achieve this is to generate SSH keys (with the private key on the local and remote hosts, and the public key on the intermediate host) and create an entry in your `~/.ssh/config` file on the local and remote hosts specifying the intermediate host parameters like the following:

```
	Host synchost # The host id can be anything as long as the local and remote match
		Hostname host1.example.com
		User jdoe
		Port 22
		IdentityFile ~/.ssh/id_rsa_jdoe # This is the private key
```


3. Copy the `.bbedit.shell` file to your remote host and source it in your `.bashrc` or `.zshrc` file by adding this line to the end of the file: `source ~/.bbedit.shell`  If you use `sudo` you'll need to add this to the root's `.bashrc` or `.zshrc` file as well. Change the two variables at the top of the file to match your environment. The directory you specify in `.bbedit.shell` must already exist on the intermediate host.

4. Copy the `Remote-BBEdit.py` file to `$HOME/Library/ApplicationSupport/iTerm2/Scripts/AutoLaunch` on the local host. This will cause the script to run every time you start iTerm2.

## How to Use ##

SSH from the local host to the remote host then enter `bbedit README.md` . This will open a BBEdit window with the `README.md` file ready for editing. When you're done in BBEdit, save and close the file. If you don't close the file, the script will not know that you're finished editing the file. After closing the file in BBEdit, the command prompt will return on the remote host.

This script does not rely on iTerm2's shell integration features, so it can safely be used inside `tmux` or `shell`. It can also be used when making multiple SSH hops between the local and remote hosts as long as the final host has access to the intermediate host.

## Limitations ##

While you can have different remote hosts utilize different intermediate hosts, all intermediate hosts must be accessible by the local host.

The remote shell command cannot be backgrounded. If you want to open the file for editing and continue working in the remote shell, you must use `tmux` with iTerm's shell integration. The local host must be able to send a keystroke back to the remote shell process to indicate that it is done editing the file, and it can only do that if it is running in an active terminal window. (If you absolutely must background the remote shell task, you can manually type `shift-Y` after bringing the task back to the foreground to tell the process that you're done editing and have saved and closed the file.)

You can only edit one file at a time. If you invoke the command a second time, the request will queue up, and the second file won't open until you close the first file. Hopefully, this issue will be resolved in a future releae.

You can't transfer changes to the file back to the remote host without closing the file. That means that if you want to see the result of your changes and then make more modifications to the file, you must close and re-open the file each time. A fix for this is planned for a future release as well.