#!/usr/bin/env ruby
# This script matches string that starts with h, ends with n

puts ARGV[0].scan(/^h.n$/).join
