exec { 'create_school_file':
    command => '/bin/echo "I love Puppet" > /tmp/school && /bin/chmod 0744 /tmp/school && /bin/chown www-data:www-data /tmp/school',
    path    => '/usr/bin:/bin',
    creates => '/tmp/school',
}
