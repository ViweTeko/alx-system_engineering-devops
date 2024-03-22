# Ensure python3.8 is installed
package { 'python3':
  ensure => 'installed',
}

# Install flask from pip3
package { 'flask':
  ensure  => '2.1.0',
  provider => 'pip3',
  before  => Exec['downgrade_werkzeug'],
}

# Downgrade Werkzeug to a specific version
exec { 'downgrade_werkzeug':
  command => 'pip3 install werkzeug==2.1.1',
  path    => '/usr/bin',
# Check's version if 2.1.1 before downgrading
unless  => 'pip3 show werkzeug | grep -q "Version: 2.1.1"'
}
