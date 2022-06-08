#!/bin/bash
export DISPLAY=:1
/usr/bin/gnome-terminal -- bash -c 'cd /root/workspace/ayachan/sanno-web-check; source $PWD/.venv/bin/activate; echo "loaded virtual env"; sleep 1; python app.py; echo "ran app.py"; echo "done"; sleep 2;'
