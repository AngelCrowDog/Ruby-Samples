require 'csv'
require 'digest'
require 'net/http'
require 'date'

LOG_ERROR = 0.freeze
LOG_SUCCESS = 1.freeze
LOG_INFO = 2.freeze

DATE_RUN  = DateTime.now.freeze
DATE_RUN_STRING = DATE_RUN.strftime('%Y%m%dT%H%M%S%L').freeze

def print_status(log_type, **opts)
	log_string = "#{opts}"
	puts "#{log_type}: #{log_string}"
	case log_type
	when LOG_ERROR
		@error_file.puts log_string
	when LOG_SUCCESS
		@success_file.puts log_string
	end
	@log_file.puts log_string
end	

	filename = "purchase_events.csv"
	filename_out = filename.gsub(/\.csv/, '')
	filename_out = "#{filename_out}_#{DATE_RUN_STRING}_"
	@success_file = File.open("#{filename_out}_success.csv", 'w')
	@log_file = File.open("#{filename_out}_log.csv", 'w')
	@error_file = File.open("#{filename_out}_error.csv", 'w')


	i = 0 

	file = CSV.read(filename, :headers=>false).each do |f|	

		begin

		url = f[0]
		data = {:url=> url}
		uri = URI.parse(URI.escape(url))
		results = Net::HTTP.get(uri)
		puts results

	if results['success":true']
		print_status(LOG_SUCCESS, data.merge(results: results))
	else
		print_status(LOG_ERROR, data.merge(results: results))
	end	
      		# i = i+1
			
			# sleep 1 if i % 100 == 0	
		end

	end	