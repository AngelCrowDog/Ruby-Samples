#V's Amazing API Script in Ruby Flavor
require_relative 'ff_loyalty'
require 'csv'
require 'digest'
require 'json'
require 'securerandom'


##########
#Accounts#
##########

	# VProd
	# ffl = FFloyalty.new('AoWuRyP22rp9gL1', 'tgkX72b4bb2tGQWWdkmdk9gIlIb8SDB0', :exec_api => true, :verbose => true, :env => "production")

	#VStage
	# ffl = FFloyalty.new('AoWuRyP22rp9gL1', 'tgkX72b4bb2tGQWWdkmdk9gIlIb8SDB0', :exec_api => true, :verbose => true, :env => "production")

	## RStage
	@ffl = FFloyalty.new('REKox9tmwkIv9rJ', 'GPNbmkL4zsuKMIJbeotAYqjzs6t2Wl3s', :exec_api => true, :verbose => true, :env => "stage")
	## RStage

	##EB PROD##
	# ffl = FFloyalty.new('ViKBE6iVVfpJgrq', 'M9dIsGNkm38XeouFKvqvAXCNEUyYtYhd', :exec_api => true, :verbose => true, :env => "production")
	##EB PROD##

	##EB UAT##
	# ffl = FFloyalty.new('ViKBE6iVVfpJgrqffl', 'M9dIsGNkm38XeouFKvqvAXCNEUyYtYhd', :exec_api => true, :verbose => true, :env => "production")
	##EB UAT##
	
	## HOLLISTER TEST##
	# ffl = FFloyalty.new('4BIij6TMOzj8YWp', 'RDCpjxKv83t3CbcDUgPV9bVhRuhfIzwa', :exec_api => true, :verbose => true, :env => "production")
	## HOLLISTER TEST##

	##KIEHL'S DEVELOPMENT##
	# ffl = FFloyalty.new('mscpA3eIjn4OwEv', '6iz8mCBkfhrDmkMyvtEFPiB4JWqdEQuA', :exec_api => true, :verbose => true, :env => "production")
	##KIEHL'S DEVELOPMENT##

	##KIEHL'S PROD REPLICA On STAGE 	ACCT 224##
	# ffl = FFloyalty.new('N0agfCNhAmylh9U', 'wtXjKiQMJscEpMg8uMQx4eHSRDQwtj8m', :exec_api => true, :verbose => true, :env => "stage")
	##KIEHL'S PROD REPLICA On STAGE		ACCT 224##

	## STEELERS NATION UNITE PROD##
	# ffl = FFloyalty.new('19xLYX1wnmmA7xr', '6BLNBuwKMyRraYGQS93ovh2AWceiSTsL', :exec_api => true, :verbose => true, :env => "production")
	## STEELERS NATION UNITE PROD##

	## GEOFF'S STORE STAGING##
	# ffl = FFloyalty.new('LZZoPur3u7wz6Ru', 'L6ZY9cpZ5xd8ktnYXMbQd7YJAoDfSAvh', :exec_api => true, :verbose => true, :env => "stage")
	## GEOFF'S STORE STAGING##

	## URBAN DECAY DEVELOPMENT##
	# ffl = FFloyalty.new('T8MKqHGj3wgUnIQ', '4oqI4CP73ZdN2pBYbsCvoa3IkukHnlA5', :exec_api => true, :verbose => true, :env => "production")
	## URBAN DECAY DEVELOPMENT##

	## OMAHA STAGING##
	# ffl = FFloyalty.new('HdxWRMWEqKhFmqQ', 'mPGlroVOmfwgxEtwfzy99rnvRb0jAJhE', :exec_api => true, :verbose => true, :env => "stage")
	## OMAHA STAGING##

	## VLAD STAGING##
	# ffl = FFloyalty.new('POvS6bcnMxOYLn8', '4KNeVqdcDgfMEfxgvKcn13FXU5RmMcl6', :exec_api => true, :verbose => true, :env => "stage")
	## VLAD STAGING##

	## JENNIFER PRODUCTION ##
	# ffl = FFloyalty.new('uD6EM2ztK5uFXpA', 'HVYdBUyYFpH4SUnMFvw1vUzkxbkC9P11', :exec_api => true, :verbose => true, :env => "production")
	## JENNIFER PRODUCTION ##

	## BUILD TEST ##
	# ffl = FFloyalty.new('gPoT81O2lrs5HWM', 'J6kA4oJjfY7EdESJt3nY6qfFHTyeC0BP', :exec_api => true, :verbose => true, :env => "production")
	## BUILD TEST ##

	## APW ##
	# ffl = FFloyalty.new('IhIGAIJ89IN4gf2', 'LijsbaU7Fr3MlAfjS4f5ho5FXLGpCEQK', :exec_api => true, :verbose => true, :env => "production")
	## APW ##

	## Urban Decay STAGING ##
	# ffl = FFloyalty.new('ZlQDOkMraQi37he', 'BAC40B6udGRB9LuY3eNqMEfqx1K0HpDY', :exec_api => true, :verbose => true, :env => "stage")
	## Urban Decay STAGING ##

	DATE_RUN = DateTime.now.freeze.strftime('%Y%m%d')

		

		options ={
		 	email: 'test@test.com'
		}
		 	
		results = @ffl.run("data/customer/show", options)
		
		# if  results['data']['code'] == 102
		# 	enroll = @ffl.run("api/enroll", options)
		# 	puts "Enrolled #{options[:email]} | #{enroll}"
		# elsif results['data']['status']['active'] 
		# 	 puts "Skipping because customer #{results['data']['status']}"
		# else results['data']['status']['paused']
		# 	activate = @ffl.run("api/reactivate", options)
		# 	puts "Activated #{options[:email]} | #{activate}"		
			
		# end

puts results





########
#ARRAYS#
########	
			# products: { '2' => { 'product_id' => '1813', 'tags' => 'RTL2XPTS' } }	 	
		 

