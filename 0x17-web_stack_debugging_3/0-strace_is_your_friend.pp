# Fixes bad PHP extension in the WordPress file 'wp-setting.php'

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g/var/www/html/wp-setting.php',
  path    => '/usr/local/bin/:/bin/'
}
