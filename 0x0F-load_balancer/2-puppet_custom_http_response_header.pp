# automate the task of creating a custom HTTP header response
exec { 'update' :
  command  => 'sudo apt-get -y update',
  provider => shell,
}

package { 'nginx' :
  ensure => installed,
}

exec { 'add header' :
  command  => 'sudo sed -i "/listen 80 default_server;/a add header X-Server-By $HOSTNAME;" /etc/nginx/sites-available/default;',
  provider => shell,
}

exec { 'nginx restart' :
  command  => 'sudo service nginx restart',
  provider => shell,
}
