require 'securerandom'
#LOY10s_5_efb34_jn16
unique ={}
20000.times do |code|
unique_code = 'LOY20s_1_' + SecureRandom.hex.to_s[0..4] + '_oct16'
unique[unique_code] = unique_code unless unique.has_key? unique_code
end
File.open("kl_01025_prod_6.csv", 'w') do |f|
unique.each do |p|
f.puts p[0]
end
end