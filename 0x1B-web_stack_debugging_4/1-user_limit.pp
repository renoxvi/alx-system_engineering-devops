# Increase the limit for open file descriptors for the 'holberton' user
user { 'holberton':
  hard => 'nofile=65535',
  soft => 'nofile=65535',
}
