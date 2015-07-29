#!/usr/bin/env python
# Authors: Mateusz Pawlowski, Jaanus Torp
# Licence: GPL-2

import argparse
import boto
import boto.ec2.autoscale
import boto.cloudformation
from random import shuffle
aws_regions = ['eu-central-1', 'sa-east-1', 'ap-northeast-1', 'eu-west-1', 'us-east-1', 'us-west-1', 'us-west-2', 'ap-southeast-2', 'ap-southeast-1']

parser = argparse.ArgumentParser(description='Returns the members of an Auto Scaling Group.')
parser.add_argument('--region', choices=aws_regions, help='AWS region', required=True)
parser.add_argument('--role', help='Role tag', required=False)
parser.add_argument('--location', help='Location tag', required=False)
parser.add_argument('--envid', help='EnvId tag', required=False)
arguments = parser.parse_args()

region = arguments.region

output = ''
asg = []
our_filters = {}

if arguments.role: 
    our_filters["tag:Role"] = arguments.role
if arguments.location: 
    our_filters["tag:Location"] = arguments.location
if arguments.envid: 
    our_filters["tag:EnvId"] = arguments.envid


ec2conn = boto.ec2.connect_to_region(region)
instance_ids = []
reservations = ec2conn.get_only_instances(filters=our_filters )
shuffle(reservations)
for instance in reservations:
    if instance.private_ip_address:
         output = ' ' +  instance.private_ip_address + output
print output

