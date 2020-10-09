#Nagios
ansible.cfg
group vars
  all
hosts 
README.MD

roles
 httpd
 nginx
     tasks/main.yml
     templates/something.j2
     vars/main.yml
     meta/main.yml 
     files/h5bp
     handlers/main.yml
  snmp-config
     tasks/main.yml
     templates/something.j2
     vars/main.yml
     meta/main.yml #file creates a dependency on the "sslcertificates"
     handlers/main.yml
     files
   install-nagios
   nagios-plugins
   install-nconf
   nconf-postinstall
   create-nagios-user
   infraplugin-config
   nagios-postinstall
server.yml

ansible-playbook --syntax-check server.yml
