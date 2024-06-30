#!/bin/bash

# Update the package list
sudo apt-get update

# Install MySQL server
sudo apt-get install -y mysql-server

# Start MySQL service
sudo systemctl start mysql

# Enable MySQL to start on boot
sudo systemctl enable mysql

sudo systemctl status mysql
