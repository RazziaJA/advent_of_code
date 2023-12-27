inputfile = "input.txt"

# Game 1: 13 red, 18 green; 5 green, 3 red, 5 blue; 5 green, 9 red, 6 blue; 3 blue, 3 green
regex = /Game (?<gamenum>\d+): (?<hands>(?<red>\d+) red, (?<blue>\d+) blue, (?<green>\d+) green;)+/

games = []
File.foreach(inputfile).each do |line|
  next if line.strip.empty?

  gamenum = line.split(": ")[0].split(" ")[1].to_i
  hands = line.split(": ")[1].split("; ")
  games.append({num: gamenum, hands: [], maxred: 0, maxblue: 0, maxgreen: 0 })
  hands.each do |handstr|
    hand = {red: 0, blue: 0, green: 0}
    handstr.split(", ").each do |cube|
      num, color = cube.split(" ")
      hand[:red] = num.to_i if color == "red"
      hand[:blue] = num.to_i if color == "blue"
      hand[:green] = num.to_i if color == "green"
    end
    games.last[:hands].append(hand)
    games.last[:maxred] = hand[:red] if hand[:red] > games.last[:maxred]
    games.last[:maxblue] = hand[:blue] if hand[:blue] > games.last[:maxblue]
    games.last[:maxgreen] = hand[:green] if hand[:green] > games.last[:maxgreen]
  end
end

# 12 red, 14 blue, 13 green
puts "Part 1:"
puts ((games.filter do |game|
  game[:maxred] <= 12 && game[:maxblue] <= 14 && game[:maxgreen] <= 13
end).map { |game| game[:num]}).sum

puts "Part 2:"
puts (games.map do |game|
  game[:maxred] * game[:maxblue] * game[:maxgreen]
end).sum