# 1-user_limit.pp

# Define a custom resource type for adjusting file descriptor limits
define file_limit {
  file { "/etc/security/limits.d/$name.conf":
    ensure  => present,
    content => "session required pam_limits.so\n$name hard nofile 4096\n",
  }
}

# Apply the file_limit resource for the holberton user
file_limit { 'holberton': }
