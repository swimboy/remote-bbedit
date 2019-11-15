function bbedit {
	synchost="sync.example.com"
	syncdir="bbedit"
	rsync "$@" "$synchost:$syncdir"
	printf "\033]1337;Custom=id=%s:%s\a" "remote-bbedit" "sftp://$synchost:/$syncdir/$@"
	read -k1 -s
	rsync --remove-source-files "$synchost:$syncdir/$@" .
}