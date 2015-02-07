# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define "statserver" do |statserver|
    statserver.vm.box = "ubuntu/trusty64"
    statserver.vm.network :private_network, ip: "192.168.33.30"

    statserver.vm.provision "ansible" do |ansible| 
      ansible.playbook = "statserver.yml"
    end 
  end

  config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--memory", "2048"]
  end

end
