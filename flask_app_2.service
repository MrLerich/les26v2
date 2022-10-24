[Unit]
Description=Flask app service description
After=network.target

[Service]
WorkingDirectory=/home/vlarin/app_inst
ExecStart=/home/vlarin/appapp_inst/venv/bin/python -m gunicorn run:app -b 0.0.0.0:80 -w 4

[Install]
WantedBy=multi-user.target