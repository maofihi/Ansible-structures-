#Nagios
ansible.cfg
group vars
  all
hosts 
README.MD
roles
  nginx
     tasks/main.yml
     templates/something.j2
     vars/main.yml
     meta/main.yml #file creates a dependency on the "sslcertificates" role
     files/h5bp
     handlers/main.yml
  snmp-config
     tasks/main.yml
     templates/something.j2
     vars/main.yml
     meta/main.yml #file creates a dependency on the "sslcertificates" role
     files/h5bp
     handlers/main.yml
   install-nagios
   nagios-plugins
   install-nconf
   nconf-postinstall
   create-nagios-user
   infraplugin-config
   nagios-postinstall
server.yml

ansible-playbook --syntax-check nagios.yml
