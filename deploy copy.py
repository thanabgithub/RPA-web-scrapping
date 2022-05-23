#!/usr/bin/bash
gnome-terminal -- bash -c 'source $PWD/.venv/bin/activate; echo "loaded virtual env"; sleep 1; python app.py; echo "ran $PWD/.venv/python"; echo "done"; sleep 2; read'