#!/usr/bin/env ruby
# This script outputs: [SENDER], [RECEIVER], [FLAGS] to run some stats

Format = ARGV[0].scan(/from:(.\w+)|to:(.\w+)|flags:([0-9:-]+)/)
List = [Format[0].compact, Format[1].compact, Format[2].compact]
puts List.join(',')
