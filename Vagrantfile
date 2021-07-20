$script = <<SCRIPT
sudo apt update
sudo apt install python3-pip -y
sudo pip3 install nose
sudo pip3 install Faker==1.0.1
sudo pip3 install pandas
sudo pip3 install matplotlib
sudo pip3 install numpy
sudo pip3 install networkx
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-20.04"
  config.vm.provision "shell", inline: $script
end

