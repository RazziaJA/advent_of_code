inputfile = "input.txt"

sum = 0
File.foreach(inputfile).each do |line|
  next if line.strip.empty?
  digits = line.each_char.find_all { |c| c =~ /\d/ }
  n = (digits[0].to_s + digits[-1].to_s).to_i
  sum = sum + n
end

puts "Part 1: #{sum}"

part_2_sum = 0;
patterns = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
regex = /(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))/
File.foreach(inputfile).each do |line|
  next if line.strip.empty?
  matches = line.scan(regex)
  first = matches.first[0]
  last = matches.last[0]
  firstn = words.index(first)
  firstn = digits.index(first) if firstn.nil?
  lastn = words.index(last)
  lastn = digits.index(last) if lastn.nil?
  n = (firstn.to_s + lastn.to_s).to_i
  part_2_sum = part_2_sum + n
end

puts "Part 2: #{part_2_sum}"