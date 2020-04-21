
I'm putting this out as an example of using systemd timers for somewhat complex intertwined operations. 

The goals are: 

Backup every hour

Run Restic's check daily 

Run Restic's prune weekly

Run Restic's full restore test quarterly 

Send failure messages via Telegram

Backups and daily checks can run concurrently, but full restore tests can't (my backup machine's tiny IO bus can't handle it)
