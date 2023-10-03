#!/usr/bin/env ruby
## Check if an argument is provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# Get the argument
input_string = ARGV[0]

# Define the regular expression
pattern = /School/

# Match the input string against the regular expression
matches = input_string.scan(pattern)

# Print the matches with the desired format
puts matches.join("$")
