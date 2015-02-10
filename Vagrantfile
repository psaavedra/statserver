# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.ssh.insert_key = false

  config.vm.provision "ansible" do |ansible|
    ansible.groups = {
      "graphiteservers" => ["statserver"],
      "sentryservers" => ["statserver"],
    }
    ansible.playbook = "site.yml"
    ansible.limit = 'all'
  end

  config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--memory", "2048"]
  end

  config.vm.define "statserver" do |statserver|
    statserver.vm.box = "ubuntu/trusty64"
    statserver.vm.hostname = "statserver"
    statserver.vm.network :private_network, ip: "192.168.33.30"
  end

end
