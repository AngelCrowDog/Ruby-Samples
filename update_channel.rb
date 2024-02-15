require_relative 'ff_loyalty'
require 'csv'
require 'digest'


LOG_ERROR = 0.freeze
LOG_ACTIVATE = 1.freeze
LOG_INFO = 2.freeze
LOG_UPDATE = 3.freeze
LOG_ENROLL = 4.freeze
LOG_SKIPPED = 5.freeze

DATE_RUN  = DateTime.now.freeze
DATE_RUN_STRING = DATE_RUN.strftime('%Y%m%dT%H%M%S%L').freeze

def print_status(log_type, **opts)
	log_string = "#{opts}"
	puts "#{log_type}: #{log_string}"
	case log_type
	when LOG_ERROR
		@error_file.puts log_string
	when LOG_ENROLL
		@enroll_file.puts log_string
	when LOG_UPDATE
		@update_file.puts log_string
	when LOG_SKIPPED
		@skipped_file.puts log_string
	end
	@log_file.puts log_string
end	

	# @ffl = FFloyalty.new('REKox9tmwkIv9rJ', 'GPNbmkL4zsuKMIJbeotAYqjzs6t2Wl3s', :exec_api => true, :verbose => true, :env => "stage")
	@ffl = FFloyalty.new('Clj4byLBGxzZJIT', 'wh1mD3OzZoNkI6mWK3Wva12YlcGPbCly', :exec_api => true, :verbose => true, :env => "production")

	filename = "1bx.csv"
	filename_out = filename.gsub(/\.csv/, '')
	filename_out = "#{filename_out}_#{DATE_RUN_STRING}_"
	@log_file = File.open("#{filename_out}_log.csv", 'w')
	@error_file = File.open("#{filename_out}_error.csv", 'w')
	@enroll_file = File.open("#{filename_out}_enrolled.csv", 'w')
	@update_file = File.open("#{filename_out}_updated.csv", 'w')
	@skipped_file = File.open("#{filename_out}_skipped.csv", 'w')

	file = CSV.read(filename, :headers=>false).each do |f|

		begin 

			email = f[0]
			first_name = f[1]
			last_name = f[2]
			home_phone = f[3]
			mobile_phone = f[4]
			sub_channel = f[5]
			channel = f[6]
			brand = f[7]

			options ={
		 	email: email,
		 	first_name:  first_name,
			last_name:  last_name,
			home_phone:  home_phone,
			mobile_phone:  mobile_phone,
			sub_channel:  sub_channel,
			channel:  channel,
			brand:  brand
		}



		results = @ffl.run("data/customer/show", options)

		if results['success'] == true		
			status = results['data']['status']
			puts status
			case status
				when 'active' 
					puts "Skipped active customer"
					print_status(LOG_SKIPPED, options)
				when 'inactive'
					enroll = @ffl.run("api/enroll", options)
					puts "Member no longer inactive, now going to update customer."
					update = @ffl.run('data/customer/update_customer_info', options)
					puts "Updated customer."
					print_status(LOG_ENROLL, options.merge(enroll: enroll))
					print_status(LOG_UPDATE, options.merge(update: update))
			end
		else
			enroll = @ffl.run("api/enroll", options)
			puts "Enrolled new customer"
			print_status(LOG_ENROLL, options.merge(enroll: enroll))
		end
		rescue => e			
			print_status(LOG_ERROR, options.merge(results: results))
		end
	end

