#!/usr/bin/env ruby
puts ARGV[0].scan(/^(\+0?1\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$/).join
