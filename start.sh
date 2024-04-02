#!/usr/bin/bash

# Setup listeners 
tmux new-session -d -s listeners

tmux new-window -t listeners:1 -n 'Daemon' '/home/belleat/Button/Daemon/flicd -f /home/belleat/Button/Daemon/flic.sqlite3'
tmux new-window -t listeners:2 -n 'Listener' '/home/belleat/Button/button.py'

# Setup app
cd /home/belleat/Button/Belleatdashboard
tmux new-session -d -s app

tmux new-window -t app:1 -n 'Backend' 'DEBUG=express:* /usr/bin/node src/backend/server.js'
tmux new-window -t app:2 -n 'Frontend' '/usr/local/bin/ng serve'
