$script = <<SCRIPT
sudo apt update
sudo apt install python3-pip -y
sudo pip3 install nose
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-20.04"
  config.vm.provision "shell", inline: $script
end

