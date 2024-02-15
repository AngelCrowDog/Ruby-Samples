#!/usr/local/bin/python3
# for python 3
# version 1.0a2


import sys
sys.path.append('/Users/vangel/Documents/ffloyalty_api/python 3')
sys.path.append('/Users/vangel/Documents/ffloyalty_api/python 3')
from FFloyalty import FFloyalty

# for making random event ids
import random
import string
import time, datetime

def rand_event_id():
	return ''.join(random.choice(string.digits) for x in range(14))


DEBUG=True
EXEC_API=True
 

def get_ffl(acct):

	if acct == 'APW':
		UUID = 'IhIGAIJ89IN4gf2'
		SECRET_KEY = 'LijsbaU7Fr3MlAfjS4f5ho5FXLGpCEQK'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)

	if acct == 'APWStage':
		UUID = 'ATv6DkvWa3xZCiE'
		SECRET_KEY = '6Y1HEMUXByTfeEBeYufnYJBoHyB1meXm'
		ENV = 'stage'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)			
		
	if acct == 'APWTest':
		UUID = 'BA9t9HMhtym7hoP'
		SECRET_KEY = 'VTV8fQ6w1JtPXtftKUIU5i1gSSnGI50Z'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	

	if acct == 'APWSanity':
		UUID = 'EIrQW5OQqu1dZ7i'
		SECRET_KEY = 'lOkdh0ATMEX9qStKMVcMC7UC5j9Z5OO1'
		ENV = 'stage'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	
		
	if acct == 'Andra':
		UUID = 'QoKCr2Od1KfksUf'
		SECRET_KEY = '2t9C5JomVyFEWjdL82O620Nk3el9Guto'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)											
				
	if acct == 'AriatTest':
		UUID = 'dEsPhf0bgo1VNx1'
		SECRET_KEY = 'EBjf6Oslh7byw3Sf3jApbkLyFynxkq1N'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)		
		
	if acct == 'BonnieStage':
		UUID = '56LHtnmIY7dfRYG'
		SECRET_KEY = 'Kqs4GDuKvuRSkghDPtUQ9wiNQNShCGwA'
		ENV = 'stage'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=DEBUG, exec_api=EXEC_API)
		
	if acct == 'build':
		UUID = 'E4F8SFG3hvGVSJz'
		SECRET_KEY = '9PDBr1ws5NKbG0vhYLlmYd9PJ3omlyoV'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	

	if acct == 'buildtest':
		UUID = 'gPoT81O2lrs5HWM'
		SECRET_KEY = 'J6kA4oJjfY7EdESJt3nY6qfFHTyeC0BP'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	
		
	if acct == 'cardstore':
		UUID = 'WWuXNHNMxbglEqu'
		SECRET_KEY = 'luNNfHem8HoTZgbzkZHi2Ny6B2eftq1P'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)				
					
	if acct == 'docs':
		UUID = 'pGbOhF3L6eCarNw'
		SECRET_KEY = 'xCaMqDsferNxExkgBEVD2kFVSuOLWI9W'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)
	
	if acct == 'Fresh':
		UUID = 'deM20cmlensD3s5'
		SECRET_KEY = 'B0ilKCiiycKwEvB28C4tovrgDUVq2Pap'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)
		
	if acct == 'FreshDev':
		UUID = '7NHCV0ciVfz2Bd7'
		SECRET_KEY = 'oTK9pi3CMYtrmna9Zeq2e9V8RWjNSkgr'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)		
		
	if acct == 'Flowers':
		UUID = 'Clj4byLBGxzZJIT'
		SECRET_KEY = 'wh1mD3OzZoNkI6mWK3Wva12YlcGPbCly'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=False)	

	if acct == 'FlowersStage':
		UUID = 'FqRZ3tvbtgSbuEA'
		SECRET_KEY = 'tFa12Zr8vce0CWFJWcQ2VdJx8OFp4l82'
		ENV = 'stage'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	
				
	if acct == 'KiehlsDev':
		UUID = 'mscpA3eIjn4OwEv'
		SECRET_KEY = '6iz8mCBkfhrDmkMyvtEFPiB4JWqdEQuA'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)

	if acct == 'KiehlsProd':
		UUID = 'zhXyRLuMiR8f8us'
		SECRET_KEY = '5RD2QHLLilKfozSahtInlRUuZSknc23m'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)			
		
	if acct == 'VProd':
		UUID = 'AoWuRyP22rp9gL1'
		SECRET_KEY = 'tgkX72b4bb2tGQWWdkmdk9gIlIb8SDB0'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)		
		
	if acct == 'VProdTest':
		UUID = 'AoWuRyP22rp9gL1'
		SECRET_KEY = 'tgkX72b4bb2tGQWWdkmdk9gIlIb8SDB0'
		ENV = 'test'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)
				
	if acct == 'BonnieProd':
		UUID = 'yYSt4f6LFqpljA1'
		SECRET_KEY = 'g8FMh7KuRlBAwdFdqoDrrForSpK4eguI'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)				
		
	if acct == 'NBProd':
		UUID = 'zzH8aExEjWHnY3x'
		SECRET_KEY = 'HinMeTNDJcX5i90FzdG1oKsgU73afVlt'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	
				
	if acct == 'Dermalogica':
		UUID = 'yzLmIV9OfRViiVD'
		SECRET_KEY = 'VRZdeuq251GlbLZGka3wY7QEgo8GMY33'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)
		
	if acct == 'DermIre':
		UUID = 'SqR7OVY619G8ooh'
		SECRET_KEY = 'rmQbU5L6kVWuUp9f0qM4u2QQ6xX3J3g6'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)
		
	if acct == 'DermUK':
		UUID = 'zIjYxQHjVygm92P'
		SECRET_KEY = 'k7WhF7rtlflnI6mkC6giiRdYw3AO02KN'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)		
		
	if acct == 'DermAu':
		UUID = 'jGkGYEbnOK2O5qD'
		SECRET_KEY = '5bwmiuveBJGfVtnpKAl9RmCYeS2MFj0b'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	
				
	if acct == 'APDev':
		UUID = '90ZdVDi2ICuK9w2'
		SECRET_KEY = 'L7pONqoWYUDbVYdlKB0DYIE2vz7nFDrh'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)		

	if acct == 'MusicNotes':
		UUID = 'YhuPhUDrhf3v8c7'
		SECRET_KEY = 'F8aJRFK7Yln63Yd9FcaGbqwAqIqDX9HO'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)		
	
	if acct == 'BonnieProd':
		UUID = 'YhuPhUDrhf3v8c7'
		SECRET_KEY = 'F8aJRFK7Yln63Yd9FcaGbqwAqIqDX9HO'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)		

	if acct == 'NBDev':
		UUID = 'dnePg7vhnPH5T8v'
		SECRET_KEY = 'wXBQLtpGkVDlvM9AU7Oyl9h4y3kBahkL'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)		

	if acct == 'ABFTest':
		UUID = 'Mjh5Sfkgw5ZsK9x'
		SECRET_KEY = 'ai882AIJA9mgtmSTB0rgQAFHiPO3t0Fs'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)		
		
	if acct == 'OmahaDev':
		UUID = 'co6qNmzNebYCDDo'
		SECRET_KEY = 'qJJDIOvJFtN3X8rpeP3rkYvnUTzPImAO'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)		
		
	if acct == 'AP':
		UUID = 'Vpuq2Iiw8pvucM8'
		SECRET_KEY = 'I6m4ZVh8Lq3Sd4F6gfaknnZuuN3rw3AU'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)		
		
	if acct == 'OmahaProd':
		UUID = '2S6UJqNbHCOTzpK'
		SECRET_KEY = 'c0MyWLajbXUrqnGDAJhKLYlQxT44rh8v'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	

	if acct == 'OmahaStage':
		UUID = 'HdxWRMWEqKhFmqQ'
		SECRET_KEY = 'mPGlroVOmfwgxEtwfzy99rnvRb0jAJhE'
		ENV = 'stage'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)			
		
	if acct == 'HCOTest':
		UUID = '4BIij6TMOzj8YWp'
		SECRET_KEY = 'RDCpjxKv83t3CbcDUgPV9bVhRuhfIzwa'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)		
		
	if acct == 'DenaProd':
		UUID = 'kZjOlPDpmJS1WUh'
		SECRET_KEY = 'yAHHuTM9BQkFlHLE8eB4noWaAwQQMOS3'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	
												
	if acct == 'HCOPromo':
		UUID = 'pyHYkJB03O6Y1hV'
		SECRET_KEY = 'UaJS39LqFHwopMMdJFNMmlPlQ0o3TV0u'
		ENV = 'test'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	

	if acct == 'HCODemo':
		UUID = 'Kx3le4D9YqGuJah'
		SECRET_KEY = 'w7bJNm8xSRAlyRVY8GDljWsf8xsmNcQc'
		ENV = 'stage'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)		

	if acct == 'KateSomervilleTest':
		UUID = '5n0NMbnnL1M9Nbo'
		SECRET_KEY = '16ecGS1lB64aT5G2R1o1RrkkeUO5Pztb'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	

	if acct == 'KS':
		UUID = 'cUhBmYAmzWK4gqO'
		SECRET_KEY = 'Ivz3YtnPBXmoC6Nr0QmqT313PjuqMAXQ'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)			
		
	if acct == 'Steelers':
		UUID = '19xLYX1wnmmA7xr'
		SECRET_KEY = '6BLNBuwKMyRraYGQS93ovh2AWceiSTsL'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)																						
		
	if acct == 'UggPromo':
		UUID = 'XlrFGol4eZtxrII'
		SECRET_KEY = 'nJaDu7sMTAJliPoytZZCkMrj0lcjNtU2'
		ENV = 'test'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	
		
	if acct == 'UnitedPetTest':
		UUID = 'nT2HOzu6Ya5Y2gq'
		SECRET_KEY = 'dqLeNqwpNMsj5wCWSFnPa7OAbPPtE4FS'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=DEBUG, exec_api=EXEC_API)				
							
	if acct == 'UggDev':
		UUID = 'd1CIzDD0PeS5ALD'
		SECRET_KEY = 'dn3c4BFavRGcQUgpJiUs8qdAWrks7xeN'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)

	if acct == 'UggInt':
		UUID = '6QFOREfp5Mdp08f'
		SECRET_KEY = '8Wt717qPk23JJLrgykQgbRmx7hThGg6s'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	

	if acct == 'UggProd':
		UUID = 'pala3GvgNJLQ2hJ'
		SECRET_KEY = 'NNRexN2uwSOUViKt68Yz98vXEEKG6sxu'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)			
			
	if acct == 'UDDev':
		UUID = 'T8MKqHGj3wgUnIQ'
		SECRET_KEY = '4oqI4CP73ZdN2pBYbsCvoa3IkukHnlA5'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)		

	if acct == 'VictoriaStage':
		UUID = 'uhwtjZtDyYuXHx7'
		SECRET_KEY = 'uulU6rWFLD7Jlf3z39xdELZYNCR54487'
		ENV = 'stage'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=DEBUG, exec_api=EXEC_API)	
		
	if acct == 'WOW':
		UUID = 'unBnQKehY2q3W7u'
		SECRET_KEY = 'VZMDEJCRlOp8g1J9s7KrQbeQyQzOz6W0'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)		

	if acct == 'fake':
		UUID = 'ABCDEFGHIJKLMNO'
		SECRET_KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEF'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=False)		

	if acct == 'UDprod':
		UUID = 'CvLwytLwwO4Iz5N'
		SECRET_KEY = 'ucgg8Q8ircP672lCRTc4vbAtYilNlHrn'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	
		
	if acct == 'HCOdev':
		UUID = 'aSC4Ow4yA35GHDG'
		SECRET_KEY = 'fqYvQbm8bepkrhSPbSNURbLe7idILIkV'
		ENV = 'stage'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	

	if acct == 'HCOProd':
		UUID = '2lwVeLzpnEkjUgK'
		SECRET_KEY = 'aln3GHeGkdpRtHoDk7UHMyHjjKjNv7g4'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)													
		
	if acct == 'JenProd':
		UUID = 'uD6EM2ztK5uFXpA'
		SECRET_KEY = 'HVYdBUyYFpH4SUnMFvw1vUzkxbkC9P11'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)

	if acct == 'AndraStage':
		UUID = 'wrrUgoFWxYajp2W'
		SECRET_KEY = 'JO65Yi1GlDkA9y7KAare52e4Nx1FhZzl'
		ENV = 'stage'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	

	if acct == 'AmberProd':
		UUID = 'LrqCV4bmxqVEY3G'
		SECRET_KEY = 'tYrac3YDkVk7PY2VVjZf1wl27xpV9AwK'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	

	if acct == 'JasonProd':
		UUID = 'TxiK5wNx2VAxGny'
		SECRET_KEY = 'oGihk69c0vuBZCDxW7UChBtkblzYkUm0'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	
		
	if acct == 'EBStage':
		UUID = 'gvpGi1ExA4ldJdD'
		SECRET_KEY = 'sThk1qNgSyPbn6bSipNC8IEut3s1983R'
		ENV = 'stage'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	
		
	if acct == 'EBDev':
		UUID = 'gvpGi1ExA4ldJdD'
		SECRET_KEY = 'sThk1qNgSyPbn6bSipNC8IEut3s1983R'
		ENV = 'stage'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	
		
	if acct == 'VStage':
		UUID = 'pGbOhF3L6eCarNw'
		SECRET_KEY = 'xCaMqDsferNxExkgBEVD2kFVSuOLWI9W'
		ENV = 'stage'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)												
			
	if acct == 'UGGUAT':
		UUID = 'PrqYOIevvUH5D40'
		SECRET_KEY = 'voCk5gJCI33vuna6ppZPIwuQFSTsEzsH'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	
		
	if acct == 'UGGSTAGE':
		UUID = 'PMt3gvU1M2i0I0y'
		SECRET_KEY = 'xSQBQlDogO0XSeG4oZWhSeDHY7wCxAAn'
		ENV = 'stage'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)														
						
	if acct == 'PPD_UAT':
		UUID = 'Fjl51P2AZ3LNoOA'
		SECRET_KEY = 'Sr7grjnrQvUTYbdl8P6roOKTHHTBU9wc'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)		

	if acct == 'cardstore_stage':
		UUID = 'oGP3v6Z4KdWc8Vl'
		SECRET_KEY = 'B6w5uFHeGI3XTndJSdakw7PXqVIlj3As'
		ENV = 'stage'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	

	if acct == 'cardstore_dev':
		UUID = 'DWadkAh0jx0imDP'
		SECRET_KEY = 'Xe1yV45DRjXxFzmrsUl5fIl4ok6BuKrg'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)																
												
	if acct == 'robert_prod':
		UUID = 'a95aeae5af2aa7'
		SECRET_KEY = 'b0513bb8cd90850b5676f0f9743b5207'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True)	
		
	if acct == 'lop_prod':
		UUID = 'bb44a8a292d3f7'
		SECRET_KEY = '21a419dc72c54cb9e8e7f33969bc019e'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True )																		

	if acct == 'nyx_uat':
		UUID = 'd878dff216ae12'
		SECRET_KEY = 'a65ae99a7d0979bd6e483244f720ac3b'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True )		

	if acct == 'ppd_uat':
		UUID = 'Fjl51P2AZ3LNoOA'
		SECRET_KEY = 'Sr7grjnrQvUTYbdl8P6roOKTHHTBU9wc'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True )		

	if acct == 'shoebuy_dev':
		UUID = 'h39E2eNWMXNDsPe'
		SECRET_KEY = 'MM67Gnk7bmlzsMu9ufu7Q2Y2K65rTncC'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True )		
		
		
	if acct == 'lancome_uat':
		UUID = '3f0ef52e832c12'
		SECRET_KEY = 'd117d36ad49e202559995b5063dc7ac3'
		ENV = 'production'
		return FFloyalty(UUID, SECRET_KEY, env=ENV, debug=True, exec_api=True )																				


															
# ffl = get_ffl('BonnieStage')
# ffl = get_ffl('DenaProd')
# ffl = get_ffl('UnitedPetTest')
# ffl = get_ffl('cardstore_dev')
# ffl = get_ffl('Fresh')
# ffl = get_ffl('FreshDev')
# ffl = get_ffl('Cache')
# ffl = get_ffl('Dermalogica')
# ffl = get_ffl('Flowers')
# ffl = get_ffl('FlowersStage')
# ffl = get_ffl('APW')
# ffl = get_ffl('APWTest')
# ffl = get_ffl('APWStage')
# ffl = get_ffl('APWSanity')
# ffl = get_ffl('build')
# ffl = get_ffl('buildtest')
# ffl = get_ffl('docs')
# ffl = get_ffl('VictoriaStage')
ffl = get_ffl('lancome_uat')
# ffl = get_ffl('VProd')
# ffl = get_ffl('shoebuy_dev')
# ffl = get_ffl('VProdTest')
# ffl = get_ffl('JenProd')
# ffl = get_ffl('BonnieProd')
# ffl = get_ffl('Steelers')
# ffl = get_ffl('KiehlsProd')
# ffl = get_ffl('KiehlsDev')
# ffl = get_ffl('NBDev')
# ffl = get_ffl('DermIre')
# ffl = get_ffl('DermAu')
# ffl = get_ffl('APStage')
# ffl = get_ffl('MusicNotes')
# ffl = get_ffl('NBDev')
# ffl = get_ffl('ABFTest')
# ffl = get_ffl('OmahaDev')
# ffl = get_ffl('OmahaStage')
# ffl = get_ffl('DermUK')
# ffl = get_ffl('AP')
# ffl = get_ffl('APDev')
# ffl = get_ffl('OmahaProd')
# ffl = get_ffl('Andra')
# ffl = get_ffl('AriatTest')
# ffl = get_ffl('HCODemo')
# ffl = get_ffl('WOW')
# fl = get_ffl('UggDev')
# ffl = get_ffl('UggInt')
# ffl = get_ffl('UggProd')
# ffl = get_ffl('UGGUAT')
# ffl = get_ffl('UGGSTAGE')
# ffl = get_ffl('HCOPromo')
# ffl = get_ffl('HCOdev')
# ffl = get_ffl('HCOProd')
# ffl = get_ffl('HCOTest')
# ffl = get_ffl('UggPromo')
# ffl = get_ffl('UDDev')
# ffl = get_ffl('UDprod')
# ffl = get_ffl('KateSomervilleTest')
# ffl = get_ffl('KS')
# ffl = get_ffl('JasonProd')
# ffl = get_ffl('AndraStage')
# ffl = get_ffl('cardstore')
# ffl = get_ffl('NBProd')
# ffl = get_ffl('AmberProd')
# ffl = get_ffl('EBStage')
# ffl = get_ffl('VStage')
# ffl = get_ffl('PPD_UAT')
# ffl = get_ffl('lop_prod')
# ffl = get_ffl('nyx_uat')
# ffl = get_ffl('ppd_uat')



# endpoint = '/api/deal_redeem'
# endpoint = '/api/enroll'
# endpoint = '/api/send_forgot_password_email'
# endpoint  = '/api/linkoffer.json'
# endpoint = '/api/pause.json'
# endpoint = '/api/record'
# endpoint = '/api/reward_redeem'
# endpoint = '/api/set_subscription_type'
# endpoint = '/api/deal_redeem'
# endpoint = '/api/unsubscribe'
# endpoint = '/api/reactivate.json'
# endpoint = '/api/upgrade_invite_only_tier'
# endpoint = '/api/referral/create'
# endpoint = '/data/referral/show'
# endpoint = '/data/referral/update'
# endpoint = '/data/customer/referrals'
# endpoint = '/data/badge_groups'
# endpoint = '/data/point_rule_groups'
# endpoint = '/data/coupon/show'
# endpoint = '/data/coupon/update'
# endpoint = '/data/deals'
# endpoint = '/data/badges'
# endpoint = '/data/event/approve'
# endpoint = '/data/event/reject'
# endpoint = '/data/events'
# endpoint = '/data/customers'
# endpoint = '/data/points/show'
# endpoint = '/data/points/value'
# endpoint = '/data/rewards'
# endpoint = '/data/reward_groups'
# endpoint = '/data/tiers'
# endpoint = '/data/customer/auth_token'
# endpoint = '/data/customer/coupons'
# endpoint = '/data/customer/events'
# endpoint = '/data/customer/merge'
# endpoint = '/data/customer/offers'
# endpoint = '/data/customer/rewards'
# endpoint = '/data/customer/badges'
endpoint = '/data/customer/show'
# endpoint = '/data/customer/update_customer_info'
# endpoint = '/data/customer/update_email'
# endpoint = '/data/customer/reward_groups'
# endpoint = '/data/customer/badge_groups'
# endpoint = '/data/customers/search'
# endpoint = '/data/customers/find'




args = {}

# args['email'] = 'vangel@stealthygoat.com'
# args['email'] = 'test1@spreadtheword.com'
# args['email'] = '500ftest@500friends.com'
# args['id'] = '99394103'
# args['uuid'] = 'mscpA3eIjn4OwEv'
# args['password'] = '2kool4skool'
# args['password_confirmation'] = '2kool4skool'
args ['external_customer_id'] = 'LAND_00000002'
# args ['create_or_update']=1


# args['from_email'] = 'veronicapinkywinkle@gmail.com'
# args['to_email'] = 'blargityblargityblarg'
# args['from_customer_id'] = '95006802'
# args['to_customer_id'] = '95031459'
# args['external_customer_id'] = '20045q34533'
# args['new_email'] = 'veronicapinkywinkle@gmail.com'
# args['nonce'] = '1459975202405Inac'



# args['after_date'] = '2016-06-26'
# args['name'] = 'Feb McBirth'
# args['enrolled_at'] = '2016-07-08'
#Above is for the blue bar, below are for profile. 
# args['first_name'] = 'Bad'
# args['last_name'] = 'Monkey'
# args['address_line_1'] = '1234 LeluDallas Multipass'
# args['address_line_2'] = ''
# args['city'] = 'Telluride'
# args['state'] = 'CO'
# args['postal_code'] = '94555'
# args['tier_id'] = 418
# args['birthdate'] = '03-22'
# args['home_store'] = '1002'
# args['phone'] = '510-845-0555'
# args['mobile_phone'] = '5555555555'
# args['work_phone'] = '5555555555'
# args['home_phone'] = ''
# args['home_store'] = 'Boston'
# args['unsubscribed'] = 'true'
# args['subscription_type'] = 'Pro'
# args['id']='74222645'
# args['tier_id']='459'
# args['deal_id']='515'
# args['status']='used'
# args['password']='abcdef'
# args['password_confirmation']='abcdef'

#EVENT TYPES
# args['type'] = 'purchase'
# args['type'] = 'return'
# args['event_type'] = 'reward'
# args['type'] = 'sms_opt_in'
# args['type'] = 'return'
# args['type'] = 'expiration'
# args['type'] = 'preferences'
# args['type'] = 'gift'
# args['type'] = 'complete_profile'
# args['type'] = 'signup'
# args['type'] = 'referral'
# args['type'] = 'share_wishlist'
# args['type'] = 'kiehls_reward'
# args['type'] = 'wishlist'
# args['type'] = 'checkin'
# args['type'] = 'Expiration'
# args['type'] = 'giver_enroll_gift'
# args['type'] = 'receiver_enroll_gift'
# args['type'] = 'monthly_gift'
# args['type'] = 'expiration'
# args['type'] = 'expiration_manual'
# args['type'] = 'review'
# args['type'] = 'badge'


#PARAMETERS
# args['value'] = '20.00'
# args['brand'] = '12345'
# args['originated_at'] = '2018-03-26T17:59:59'
# args['created_at'] = '2018-03-26T17:59:59'
# args['enrolled_at'] = '2018-01-05'
# args['expires_at'] = '3/2/18'
# args['autoenroll'] = '1'
# args['expiration_details'] = 'true'
# args['after_date'] = '2016-04-01T00:00:00-07:00'
# args['date_filter'] = 'expires_at'
# args['before_date'] = '2016-05-01T00:00:00-07:00'
# args['original_event_id'] = '20161116111859'
# args['event_id'] = '20180416095025'
# args['id'] = '834924685'
# args['enrolled_at'] = '2015-06-01'
# args['created_at'] = '2016-10-29'
# args['link_date'] = '2015-04-21'
# args['code'] = 'BVFJK6'
# args['status'] = 'used'
# args['code'] = 'LOY20_1_6c8fb_dc15'
# args['id'] = '732629072'
# args['deal_id'] = '399'
# args['reward_id'] = '1662'
# args['name'] = "Sony Bravia® XBR® 70\" LCD High Definition Television"
# args['detail'] = 'birthday reward redeemed'
# args['detail'] = 'Due to a technical issue additional Fresh Family Rewards points were added to your account. These points have been removed from your account and your balance is now accurate.  We\'re sorry for any confusion this may have caused.  Due to a technical issue additional Fresh Family Rewards points were added to your account. These points have been removed from your account and your balance is now accurate.  We\'re sorry for any confusion this may have caused.  Due to a technical issue additional Fresh Family Rewards points were added to your account. These points have been removed from your account and your balance is now accurate.  We\'re sorry for any confusion this may have caused.  Due to a technical issue additional Fresh Family Rewards points were added to your account. These points have been removed from your account and your balance is now accurate.  We\'re sorry for any confusion this may have caused.  Due to a technical issue additional Fresh Family Rewards points were added to your account. These points have been removed from your account and your balance is now accurate.  We\'re sorry for any confusion this may have caused. Due to a technical issue additional Fresh Family Rewards points were added to your account. These points have been removed from your account and your balance is now accurate.  We\'re sorry for any confusion this may have caused.Due to a technical issue additional Fresh Family Rewards points were added to your account. These points have been removed from your account and your balance is now accurate.  We\'re sorry for any confusion this may have caused.Due to a technical issue additional Fresh Family Rewards points were added to your account. These points have been removed from your account and your balance is now accurate.  We\'re sorry for any confusion this may have caused.Due to a technical issue additional Fresh Family Rewards points were added to your account. These points have been removed from your account and your balance is now accurate.  We\'re sorry for any confusion this may have caused.Due to a technical issue additional Fresh Family Rewards points were added to your account. These points have been removed from your account and your balance is now accurate.  We\'re sorry for any confusion this may have caused.Due to a technical issue additional Fresh Family Rewards points were added to your account. These points have been removed from your account and your balance is now accurate. Here is a dash.  ----- dash dash dash - dash - dash'
# args['detail']='I enroll therefore I am!'
# args['channel'] = 'retail'
# args['sub_channel'] = '10004'
# args['brand'] = 'Kiehls'
# args['purchase_dependent'] = 'true'
# args['sub_channel'] = 'lcc_harristeeter'
# args['sub_channel_detail'] = 'lcc_harristeeter'
# args['private_notes'] = 'overrode redemption restriction based on today\'s 100 point purchase'
# args['external_user_id'] = 'hcotest123'
# args['expiration_date'] = '2015-01-23T19:10:00'
# args['brand'] = 'nookie'
# args['offerid'] = '11743'
# args['entries_per_page'] = '5'
# args['page_number'] = '1'
# args['after_date'] = '20160210'
# args['before_date'] = '20160218'
# args['date_filter'] = 'last_activity'
# args['include'] = 'identities'
# args['referral_code'] = 'pk6gmsj6'
# args['product_id'] = '3605971044052'

#COUPON ARRAY
# args['event_coupons'] = {}
# args['event_coupons']['0'] = {}
# args['event_coupons']['0']['code']='246810'
# args['coupons']['1'] = {}
# args['coupons']['1']['code']='LOYALTY6s'

# TENDER ARRAY 
# args['tenders'] = {}
# args['tenders']['0'] = {}
# args['tenders']['0']['name']='visa'
# args['tenders']['0']['value']='60'
# args['tenders']['1'] = {}
# args['tenders']['1']['name']='merch_credit'
# args['tenders']['1']['value']='10'

# args ['products'] = {}
# args ['products']['0'] = {}
# args ['products']['0']['brands']= 'Dansko' 
# args ['products']['0']['price']= '100.00' 
# args ['products']['0']['product_id']= '888855879947'
# # args ['products']['1'] = {}
# args ['products']['1']['quantity']= '1' 
# args ['products']['1']['price']= '0.00' 
# args ['products']['1']['product_id']= ''
# args ['products']['2'] = {}
# args ['products']['2']['quantity']= '1' 
# args ['products']['2']['price']= '10.00' 
# args ['products']['2']['product_id']= '' 
# args ['products']['3'] = {}
# args ['products']['3']['quantity']= '1' 
# args ['products']['3']['price']= '5.99' 
# args ['products']['3']['product_id']= '889830309473'
# args ['products']['4'] = {}
# args ['products']['4']['quantity']= '1' 
# args ['products']['4']['price']= '0' 
# args ['products']['4']['product_id']= 'abcd'

# HCO 
# args['products'] = {}
# args['products']['0'] = {}
# args ['products']['0']['brands']= 'Evan+Fischer' 
# args ['products']['0']['price']= '100.00' 
# args ['products']['0']['product_id']= '123'
# args ['products']['0']['tags']= '' 
# args ['products']['0']['quantity']= '1' 
# args['products']['1'] = {}
# args ['products']['1']['quantity']= '1' 
# args ['products']['1']['price']= '50.00' 
# args ['products']['1']['product_id']= '12345'
# args ['products']['1']['tags']= 'monkey' 
# args ['products']['2'] = {}
# args ['products']['2']['brands']= 'HCO' 
# args ['products']['2']['price']= '50.00' 
# args ['products']['2']['product_id']= 'guys jeans' 
# args ['products']['2']['categories']= 'm>Hco. guys jeans' 
# args ['products']['3'] = {}
# args ['products']['3']['brands']= 'Kool%20Vue' 
# args ['products']['3']['price']= '261.5' 
# args ['products']['3']['product_id']= 'koolvuegm73el-sdriverside' 
# args ['products']['4'] = {}
# args ['products']['4']['brands']= 'Kool%20Vue' 
# args ['products']['4']['price']= '42.93' 
# args ['products']['4']['product_id']= 'koolvuegm59rpassengerside' 
# args ['products']['5'] = {}
# args ['products']['5']['brands']= 'Kool%20Vue' 
# args ['products']['5']['price']= '262.63' 
# args ['products']['5']['product_id']= 'koolvuegm73er-spassengerside' 
# args ['products']['6'] = {}
# args ['products']['6']['brands']= 'Kool%20Vue' 
# args ['products']['6']['price']= '33.97' 
# args ['products']['6']['product_id']= 'koolvuegm30erpassengerside' 
# args ['products']['7'] = {}
# args ['products']['7']['brands']= 'Kool%20Vue' 
# args ['products']['7']['price']= '482.24' 
# args ['products']['7']['product_id']= 'koolvuecv41el-sdriverside' 
# args ['products']['8'] = {}
# args ['products']['8']['brands']= 'Kool%20Vue' 
# args ['products']['8']['price']= '41.45' 
# args ['products']['8']['product_id']= 'koolvuegm30ldriverside' 
# args ['products']['9'] = {}
# args ['products']['9']['brands']= 'Kool%20Vue' 
# args ['products']['9']['price']= '70.74' 
# args ['products']['9']['product_id']= 'koolvuedg42erpassengerside'
# args ['products']['10'] = {}
# args ['products']['10']['brands']= 'Kool' 
# args ['products']['10']['price']= '67.07' 
# args ['products']['10']['product_id']= 'koolvuecv19erpassengerside' 

#Omaha
# args ['products'] = {}
# args ['products']['0'] = {}
# args ['products']['0']['tags']='RTL2XPTSA'
# args ['products']['0']['price']='50.00' 
# args ['products']['0']['product_id']='1906'
# args ['products']['0']['quantity']= '2' 
# args ['products']['1'] = {}
# args ['products']['1']['tags']='RTL2XPTSB'
# args ['products']['1']['price']='50.00' 
# args ['products']['1']['product_id']='1909' 
# args ['products']['1']['quantity']= '1' 
# args ['products']['2'] = {}
# args ['products']['2']['tags']='42662' 
# args ['products']['2']['brands']='' 
# args ['products']['2']['price']='10' 
# args ['products']['2']['product_id']='' 

#APW
# args ['products'] = {}
# args ['products']['0'] = {}
# args ['products']['0']['quantity']='1' 
# args ['products']['0']['price']='100'
# args ['products']['0']['product_id']='beckarnleybec0361788passengerside' 
# args ['products']['0']['brand']='Beck+Arnley' 
# args ['products']['1'] = {}
# args ['products']['1']['quantity']='1'
# args ['products']['1']['price']='100' 
# args ['products']['1']['product_id']='victorreinzw0133-1790268driverside,upper' 
# args ['products']['1']['brand']='Victor+Reinz' 
# args ['products']['2'] = {}
# args ['products']['2']['brands']='EvanFischer' 
# args ['products']['2']['price']='100' 
# args ['products']['2']['product_id']='SKU3' 
# args ['products']['3'] = {}
# args ['products']['3']['brands']='Centric' 
# args ['products']['3']['price']='100' 
# args ['products']['3']['product_id']='centricce105-dot-09190rear' 
# args ['products']['4'] = {}
# args ['products']['4']['brands']='Beck+Arnley' 
# args ['products']['4']['price']='55' 
# args ['products']['4']['product_id']='beckarnleybec0361788passengerside' 
# args ['products']['5'] = {}
# args ['products']['5']['brands']='Victor+Reinz' 
# args ['products']['5']['price']='10' 
# args ['products']['5']['product_id']='victorreinzw0133-1790268driverside,upper' 
# args ['products']['6'] = {}
# args ['products']['6']['brands']='Lemfoerder' 
# args ['products']['6']['price']='66' 
# args ['products']['6']['product_id']='lemfoerderw0133-1664463front,upper' 
# args ['products']['7'] = {}
# args ['products']['7']['brands']='Victor+Reinz' 
# args ['products']['7']['price']='8' 
# args ['products']['7']['product_id']='victorreinzw0133-1790267passengerside,upper' 
# args ['products']['8'] = {}
# args ['products']['8']['brands']='Beck+Arnley' 
# args ['products']['8']['price']='50' 
# args ['products']['8']['product_id']='beckarnleybec0361787driverside' 
# args ['products']['9'] = {}
# args ['products']['9']['brands']='Beck+Arnley' 
# args ['products']['9']['price']='39' 
# args ['products']['9']['product_id']='beckarnley034-0807upper' 
# args ['products']['10'] = {}
# args ['products']['10']['brands']='Beck+Arnley' 
# args ['products']['10']['price']='43' 
# args ['products']['10']['product_id']='beckarnley034-0805lower' 

# Example 12 from Product Bonus Signature Calculation Doc
# args ['products'] = {}
# args ['products']['0'] = {}
# args ['products']['0']['price']= 10
# args ['products']['0']['brands']= 'brand2'
# args ['products']['0']['categories']= 'category2>subcategory'
# args ['products']['0']['quantity']= 1
# args ['products']['0']['product_id']= 0
# args ['products']['1'] = {}
# args ['products']['1']['price']= 18
# args ['products']['1']['brands']= 'brand1,brand2'
# args ['products']['1']['categories']= 'category1,category2>subcategory'
# args ['products']['1']['quantity']= 2
# args ['products']['1']['product_id']= '1'
# args ['products']['2'] = {}
# args ['products']['2']['price']= '27'
# args ['products']['2']['brands']= 'brand1,brand2'
# args ['products']['2']['categories']= 'category1,category2>subcategory'
# args ['products']['2']['quantity']= '3'
# args ['products']['2']['product_id']= '2'
# args ['products']['3'] = {}
# args ['products']['3']['price']= '36'
# args ['products']['3']['brands']= 'brand1,brand2'
# args ['products']['3']['categories']= 'category1,category2>subcategory'
# args ['products']['3']['quantity']= '4'
# args ['products']['3']['product_id']= '3'
# args ['products']['4'] = {}
# args ['products']['4']['price']= '45'
# args ['products']['4']['brands']= 'brand1,brand2'
# args ['products']['4']['categories']= 'category1,category2>subcategory'
# args ['products']['4']['quantity']= '5'
# args ['products']['4']['product_id']= '4'
# args ['products']['5'] = {}
# args ['products']['5']['price']= '54'
# args ['products']['5']['brands']= 'brand1,brand2'
# args ['products']['5']['categories']= 'category1,category2>subcategory'
# args ['products']['5']['quantity']= '6'
# args ['products']['5']['product_id']= '5'
# args ['products']['6'] = {}
# args ['products']['6']['price']= '63'
# args ['products']['6']['brands']= 'brand1,brand2'
# args ['products']['6']['categories']= 'category1,category2>subcategory'
# args ['products']['6']['quantity']= '7'
# args ['products']['6']['product_id']= '6'
# args ['products']['7'] = {}
# args ['products']['7']['price']= '72'
# args ['products']['7']['brands']= 'brand1,brand2'
# args ['products']['7']['categories']= 'category1,category2>subcategory'
# args ['products']['7']['quantity']= '8'
# args ['products']['7']['product_id']= '7'
# args ['products']['8'] = {}
# args ['products']['8']['price']= '81'
# args ['products']['8']['brands']= 'brand1,brand2'
# args ['products']['8']['categories']= 'category1,category2>subcategory'
# args ['products']['8']['quantity']= '9'
# args ['products']['8']['product_id']= '8'
# args ['products']['9'] = {}
# args ['products']['9']['price']= '90'
# args ['products']['9']['brands']= 'brand1,brand2'
# args ['products']['9']['categories']= 'category1,category2>subcategory'
# args ['products']['9']['quantity']= '10'
# args ['products']['9']['product_id']= '9'
# args ['products']['10'] = {}
# args ['products']['10']['price']= '99'
# args ['products']['10']['brands']= 'brand1,brand2'
# args ['products']['10']['categories']= 'category1,category2>subcategory'
# args ['products']['10']['quantity']= '11'
# args ['products']['10']['product_id']= '10'
# args ['products']['11'] = {}
# args ['products']['11']['price']= '108'
# args ['products']['11']['brands']= 'brand1,brand2'
# args ['products']['11']['categories']= 'category1,category2>subcategory'
# args ['products']['11']['quantity']= '12'
# args ['products']['11']['product_id']= '11'

#APW
# args ['products'] = {}
# args ['products']['0'] = {}
# args ['products']['0']['brands']= 'ReplaceXL' 
# args ['products']['0']['part']= 'Headlight' 
# args ['products']['0']['price']= '50.00' 
# args ['products']['0']['product_id']= 'replacexlr-20-5222-00driverside' 
# args ['products']['1'] = {}
# args ['products']['1']['brands']= 'Kool Vue' 
# args ['products']['1']['price']= '50.00' 
# args ['products']['1']['product_id']= 'koolvuegm24eldriverside' 
# args ['products']['2'] = {}
# args ['products']['2']['brands']= 'Kool Vue' 
# args ['products']['2']['price']= '5.00' 
# args ['products']['2']['product_id']= 'koolvuegm30eldriverside' 
# args ['products']['3'] = {}
# args ['products']['3']['brands']= 'Kool Vue' 
# args ['products']['3']['price']= '261.5' 
# args ['products']['3']['product_id']= 'koolvuegm73el-sdriverside' 
# args ['products']['4'] = {}
# args ['products']['4']['brands']= 'Kool Vue' 
# args ['products']['4']['price']= '42.93' 
# args ['products']['4']['product_id']= 'koolvuegm59rpassengerside' 
# args ['products']['5'] = {}
# args ['products']['5']['brands']= 'Kool Vue' 
# args ['products']['5']['price']= '262.63' 
# args ['products']['5']['product_id']= 'koolvuegm73er-spassengerside' 
# args ['products']['6'] = {}
# args ['products']['6']['brands']= 'Kool Vue' 
# args ['products']['6']['price']= '33.97' 
# args ['products']['6']['product_id']= 'koolvuegm30erpassengerside' 
# args ['products']['7'] = {}
# args ['products']['7']['brands']= 'Kool Vue' 
# args ['products']['7']['price']= '482.24' 
# args ['products']['7']['product_id']= 'koolvuecv41el-sdriverside' 
# args ['products']['8'] = {}
# args ['products']['8']['brands']= 'Kool Vue' 
# args ['products']['8']['price']= '41.45' 
# args ['products']['8']['product_id']= 'koolvuegm30ldriverside' 
# args ['products']['9'] = {}
# args ['products']['9']['brands']= 'Kool Vue' 
# args ['products']['9']['price']= '70.74' 
# args ['products']['9']['product_id']= 'koolvuedg42erpassengerside'
# args ['products']['10'] = {}
# args ['products']['10']['brands']= 'Kool' 
# args ['products']['10']['price']= '67.07' 
# args ['products']['10']['product_id']= 'koolvuecv19erpassengerside' 

#HCO
# args ['tenders'] = {}
# args ['tenders']['0'] = {}
# args ['tenders']['0']['name']= 'cash' 
# args ['tenders']['0']['value']= '100.00'
# args ['tenders']['1'] = {}
# args ['tenders']['1']['name']= 'cash' 
# args ['tenders']['1']['value']= '130.0'
# args ['tenders']['2'] = {}
# args ['tenders']['2']['name']= 'GCRD' 
# args ['tenders']['2']['value']= '25.61'
# args ['tenders']['3'] = {}
# args ['tenders']['3']['name']= 'LCRD' 
# args ['tenders']['3']['value']= '20.0'


# value=0
# args['products'] = {}
# for i in range(12):
# 	args['products'][str(i)] = {}
# 	args['products'][str(i)]['brands'] = 'brand1'
# 	args['products'][str(i)]['product_id'] = str(i)
# 	args['products'][str(i)]['price'] = str(9 * (i + 1))
# 	args['products'][str(i)]['categories'] = 'category1,category2>subcategory'
# 	args['products'][str(i)]['quantity'] = str(i+1)
# 	value += (i+1)*9*(i+1)
#   args['value'] = str(value)


for i in range(1):
	args['event_id'] = '20180416095025'
# 	args['event_id'] = rand_event_id()
# 	args['email'] = str(i) + 'bonnie@the-bonnies.com'
	jout = ffl.run(endpoint, args)
	print(str(jout))

# for i in range(1):
# 	args['event_id'] = rand_event_id()
# 	args['email'] = str(i) + 'bonnie@the-bonnies.com'
# 	for i in range(100):
# 		jout = ffl.run(endpoint, args)
# 		print(datetime.datetime.now().strftime('%H:%M:%S') + ' ' + str(jout['points']) + ' points')
# 		time.sleep(1)
	