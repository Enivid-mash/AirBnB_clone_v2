#!/usr/bin/env bash
# Update packages list and install Nginx

sudo apt-get update -y && sudo apt-get install nginx -y

# Create necessary directories
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

# Set index.html page
echo "<h1>ALX SE School</h1>" | sudo tee /data/web_static/releases/test/index.html

# Link releases/test to current symlink
sudo ln -sfT /data/web_static/releases/test/ /data/web_static/current

# Change permissions for data dir
sudo chown -R ubuntu:ubuntu /data

# Edit Nginx config
sudo sed -i '$ i\    location ~ /hbnb_static { \n        alias /data/web_static/current/ ;\n    }\n' /etc/nginx/sites-available/default

# Reload Nginx service
sudo service nginx restart
