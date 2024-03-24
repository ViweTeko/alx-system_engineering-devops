# Puppet script that creates ssh config file
file_line { 'Turn off passwd auth':
  ensure => 'present',
  path   => 'etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => 'present',
  path   => 'etc/shh/shh_config',
  line   => '    IdentityFile ~/.shh/school',
}
