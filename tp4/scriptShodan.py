from shodan import Shodan

API_KEY = 'yLiKani57BJSRWs7hYnjUWGDi0Mlj8pl'
api = Shodan(API_KEY)

# 2-a
#results = api.search('port: 5900 country:AR')
#results = api.search('port:5900 country:AR has_screenshot:true')

# 2-b
#results = api.search('webcamxp country:AR')
#results = api.search('webcamxp country:AR has_screenshot:true')

# 2-c
#results = api.search('apache country:AR')
#results = api.search('apache country:BR')
#results = api.search('apache country:CL')
#results = api.search('apache country:UY')

# 2-d
#results = api.search('iomega country:AR')
#results = api.search('iomega country:BR')
#results = api.search('iomega country:CL')
#results = api.search('iomega country:UY')

# 2-e
# results = api.search('nginx country:AR')
# results = api.search('nginx country:BR')
# results = api.search('nginx country:CL')
# results = api.search('nginx country:UY')

# 2-f
# results = api.search('snmp2  country:AR')
# results = api.search('snmp2 country:BR')
# results = api.search('snmp2 country:CL')
# results = api.search('snmp2 country:UY')

# 2-g
# results = api.search('os:windows')
# results = api.search('os:windows country:AR')
# results = api.search('os:windows country:ES')
# results = api.search('os:windows country:CN')
# results = api.search('os:linux')
# results = api.search('os:linux country:AR')
# results = api.search('os:linux country:ES')