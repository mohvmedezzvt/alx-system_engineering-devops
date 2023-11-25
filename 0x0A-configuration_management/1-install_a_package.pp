# Puppet manifest to install flask from pip3.

exec { 'install_werkzeug':
  command     => '/usr/bin/pip3 install Werkzeug==2.1.1',
  path        => '/usr/local/bin',
  refreshonly => true,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => '/usr/local/bin',
  refreshonly => true,
}
