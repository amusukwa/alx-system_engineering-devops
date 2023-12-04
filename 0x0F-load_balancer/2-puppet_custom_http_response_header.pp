# 2-puppet_custom_http_response_header.pp

# Update package repositories
package { 'nginx':
  ensure => installed,
}

# Define a custom HTTP header file
file { '/etc/nginx/sites-available/custom_header':
  ensure  => file,
  content => "add_header X-Served-By $hostname;",
}

# Create a symbolic link to the sites-enabled directory
file { '/etc/nginx/sites-enabled/custom_header':
  ensure => link,
  target => '/etc/nginx/sites-available/custom_header',
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/custom_header'],
}
