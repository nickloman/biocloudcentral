import bioblend
from bioblend.util import Bunch
from bioblend.cloudman.launch import CloudManLauncher

import logging
logging.basicConfig(filename="bioblend.log", level=logging.DEBUG)


cloud = Bunch(id='1', name='climb', cloud_type="openstack", bucket_default="cloudman_os", region_name="nova", region_endpoint="147.188.173.10", ec2_port="8773", ec2_conn_path="/services/Cloud", cidr_range="147.188.173.0/24", is_secure=False, s3_host="swift.rc.nectar.org.au", s3_port="8888", s3_conn_path='/')

cml = CloudManLauncher('ACCESS_KEY', 'SECRET_KEY', cloud)

response = cml.launch(cluster_name='test',
                              image_id='ami-00000039',
                              instance_type='m1.large',
                              password='test',
                              placement='nova')

print response
