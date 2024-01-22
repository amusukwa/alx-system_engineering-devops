
# Update the configuration file for Nginx
exec { 'file-for-nginx':
  command => '/bin/sed -i "s/13/4096/" /etc/default/nginx',
  path    => '/usr/local/bin:/bin',
}

# Restart Nginx after updating the configuration
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}
