#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# Get the argument
input_string = ARGV[0]

# Define the regular expression
pattern = /School/

# Check if the input string matches the regular expression
if input_string.match?(pattern)
  puts "#{input_string}$"
else
  puts "No match"
end
