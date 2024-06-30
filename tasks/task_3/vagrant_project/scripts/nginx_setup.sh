#!/bin/bash

# Update the package list
sudo apt-get update

# Install Nginx
sudo apt-get install -y nginx

# Start Nginx
sudo systemctl start nginx

# Enable Nginx to start on boot
sudo systemctl enable nginx

sudo systemctl status nginx
