#  puppet manifest (0-strace_is_your_friend.pp)

exec { 'fix word-press':
  command  => 'sed -i s/phpp/php/g  var/www/html/wp-settings.ph,
  path  => '/usr/local/bin/:/bin'
  
}
