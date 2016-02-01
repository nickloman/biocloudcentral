from pprint import pprint

import boto.ec2
from boto.ec2.regioninfo import RegionInfo
ri = RegionInfo(name='nova', endpoint='147.188.173.10')
c = boto.connect_ec2(aws_access_key_id='ACCESS KEY', aws_secret_access_key='SECRET KEY', region=ri, port=8773, path='/services/Cloud', is_secure=0)
for i in c.get_all_images():
	print i.id, i.name

