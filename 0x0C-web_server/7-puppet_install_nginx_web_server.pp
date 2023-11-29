# 5-install_nginx_redirect_301.pp

# Install Nginx package
exec { 'update':
  command => 'app-get -y update',
  path => '/usr/bin',
}

package { 'nginx':
  ensure => installed,
  name => 'nginx',
  provider => 'apt',

}

service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}


file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
  server {
   listen 80;
   location / {
    return 200 'Hello World':
   }
   location /redirect_me {
    return 301 http://\$host
   }",
  notify => Service['nginx'],
}

exec { 'nginx_reload':
  command => '/usr/sbin/service nginx reload',
  refreshonly => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
