# ssh_config.pp

file { '/home/ubuntu/.ssh/config':
  ensure  => 'file',
  mode    => '0600',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => template('ssh/config.erb'),
}

