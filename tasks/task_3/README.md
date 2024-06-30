# Vagrant Task

## Question
INSTRUCTION: Attempt all questions. Upload your Vagrantfile onto Google Drive and share the link. Take screenshots of working commands where necessary to prove the completion of tasks. Ensure that the link you submit is accessible. 

TASKS:

With the use of a single Vagrantfile, provision two VMs named 
One VM would be for a web server and the other for a database, name accordingly 
Configure the web server VM using Shell provisioner (write the bash script in a different file and reference it using the path option)
Customize the resources of your VM: memory=1024
Setup an Nginx server on your machine
Configure the db server VM using Shell provisioner (write the bash script in a different file and reference it using the path option)
Customize the resources of your VM: memory=2048
Setup a MySQL on your machine
Both Machines should be able to communicate with each other on the network 





## Steps

### Step 1: Create the Directory Structure

First, create a directory for the Vagrant project. Inside this directory, create separate directories for the web server and database server scripts.

```bash
mkdir vagrant_project
cd vagrant_project
mkdir scripts
```

### Step 2: Create the Shell Provisioning Scripts

Created two shell scripts inside the script directory. One for setting up the Nginx server and the other for setting up MySQL.
`nginx_setup.sh`

Create and edit the nginx_setup.sh script:

```bash
nano scripts/nginx_setup.sh
```

Copy and paste the following content into the nginx_setup.sh file:

```bash
#!/bin/bash

# Update the package list
sudo apt-get update

# Install Nginx
sudo apt-get install -y nginx

# Start Nginx
sudo systemctl start nginx

# Enable Nginx to start on boot
sudo systemctl enable nginx

# Nginx status
Sudo systemctl status nginx
```

Save the file and exit the editor. Then make the script executable:
`chmod +x scripts/nginx_setup.sh`


`mysql_setup.sh`

```bash
nano scripts/mysql_setup.sh
```

Copy and paste the following content into the mysql_setup.sh file:

```bash
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
```

Save the file and exit the editor. Then make the script executable:
`chmod +x scripts/nginx_setup.sh`


### Step 3: Create the Vagrantfile

Created a Vagrantfile in the root of the vagrant_project directory:

```bash
Vagrantfile init

nano Vagrantfile or code Vagrantfile
```

Copy and paste the following content into the Vagrantfile:

```bash
  config.vm.box = "ubuntu/focal64"
   # Define the web server VM
   config.vm.define "web-server" do |web|
    web.vm.hostname = "ubuntu" 
    web.vm.network "private_network", ip: "192.168.56.10"  # Set a static IP
    web.vm.network "forwarded_port", guest: 80, host: 2323
    web.vm.provider "virtualbox" do |vb|
      vb.memory = 1024
    end


    # Provision the web server from an external file
    web.vm.provision "shell", path: "scripts/nginx_setup.sh"
  end


  # Define the database VM
  config.vm.define "database" do |db|
    db.vm.hostname = "mysql"
    db.vm.network "private_network", ip: "192.168.56.11"  # Set a static IP
    db.vm.network "forwarded_port", guest: 80, host: 1212
    db.vm.provider "virtualbox" do |vb|
      vb.memory = 2048
    end
    
    # Provision the database server
    db.vm.provision "shell", path: "scripts/nginx_setup.sh"
  end
```


### Step 4: Bring Up the VMs

Run the following command to bring up both VMs:
`vagrant up`

This will provision two VMs, one configured with Nginx and the other with MySQL, as specified in your Vagrantfile.

### Step 5: Verify the Setup

Check Nginx on the Web Server VM
SSH into the web server VM and verify Nginx is running:
`vagrant ssh web`

Once inside, you can check the status of Nginx:
`systemctl status nginx`

You can also open a web browser and navigate to http://192.168.33.10 to see the default Nginx welcome page.
Check MySQL on the Database Server VM
SSH into the database server VM and verify MySQL is running:
`vagrant ssh database`

Once inside, you can check the status of MySQL:
`systemctl status mysql`

### Step 6: Ensure Network Communication Between VMs
From the web server VM, try to ping the database server VM:
`ping 192.168.33.11`

From the database server VM, try to ping the web server VM:
`ping 192.168.33.10`

## Conclusion
Following these steps are use to provision and configure two VMs using Vagrant, one as a web server with Nginx and the other as a database server with MySQL, and can communicate with each other on the network.
