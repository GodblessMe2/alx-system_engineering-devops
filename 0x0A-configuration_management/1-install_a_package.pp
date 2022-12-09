#Install flask from pip3

package { 'flask':
  ensure   => '2.2.1',
  provider => 'pip3',
}