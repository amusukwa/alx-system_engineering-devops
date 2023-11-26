# ssh_config.pp

file { '/etc/ssh/ssh_config':
  ensure  => 'present',
}

file_line { 'Turn off password auth':
 path  => '/etc/ssh/ssh_config',
 line    => 'PasswordAuthentication no',
 match   => '#PasswordAuthentication ',
  
}

file_line { 'Declare identify file':
 path  => '/etc/.ssh/ssh_config',
 line    => 'IdentifyFile ~/.ssh/shool',
 match   => '#PasswordAuthentication ',
  
}
