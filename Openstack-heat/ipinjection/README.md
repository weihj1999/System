This section will include all the action operation, you may refer
to the examples used user_data, softconfig, and etc.

For ip operation in chef, ansible tools won't be discussed here.

The key message to get ip from the port is:

Accoring to the guide:
http://docs.openstack.org/developer/heat/template_guide/openstack.html
OS::Neutron::Port resource has an attribute fixed_ips that is a list 
of maps (aka "dictionaries"), each of which has a ip_address key. So
So, you want the ip_address key of the first item of the fixed_ips list:

$APP_HOST_IP_ENV: {get_attr: [wmwcvm1_port, fixed_ips, 0, ip_address}

