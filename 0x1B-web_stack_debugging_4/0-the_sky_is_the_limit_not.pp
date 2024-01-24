# Update the configuration file for Nginx
 exec { 'file-for-nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin:/bin',
  onlyif  => '/usr/bin/test -f /etc/default/nginx',
}

exec { 'nginx-restart':
  command => '/bin/systemctl restart nginx',
  path    => '/bin',
  refreshonly => true,
  subscribe   => Exec['file-for-nginx'],
}
