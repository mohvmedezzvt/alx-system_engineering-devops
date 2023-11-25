# Puppet manifest to configure SSH client
include stdlib

file { 'No password authentication':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    line    => 'PasswordAuthentication no',
    replace => true,
}

file { 'Configure private key':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    line    => 'IdentifyFile ~/.ssh/school',
    replace => true,
}
