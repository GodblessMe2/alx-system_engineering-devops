# Fixes bad PHP extension in the WordPress file 'wp-setting.php'
exec { 'Debugging':
  command  => 'sudo sed -i \'s/phpp/php/g\' /var/www/html/wp-settings.php && sudo service apache2 restart',
  provider => shell,
}
