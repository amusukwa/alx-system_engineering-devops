# 5-install_nginx_redirect_301.pp

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',

}

file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page",
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => template('/etc/nginx/nginx.conf'),
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
}
