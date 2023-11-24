#!/usr/bin/pup
#install flask from pip3

exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => ['/usr/bin', '/usr/local/bin'],
  refreshonly => true,
  creates     => '/usr/local/lib/python3.x/dist-packages/Flask-2.1.0.dist-info',
}
