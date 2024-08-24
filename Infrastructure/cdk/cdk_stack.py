from os import path
from aws_cdk import (aws_s3, Stack, aws_lambda, aws_iam, Duration, aws_ec2)
from constructs import Construct
import os
from os import path



class DemoStack(Stack):
    def __init__(self, scope: Construct, id:str, environment:None, **kwargs) -> None:
        super().__init__(scope,id,**kwargs)

#         # Create a VPC
#         vpc = aws_ec2.Vpc(self, "MyVpc",
#          max_azs=3,  # Default is all AZs in the region
#                               cidr="10.0.0.0/16",
#                               subnet_configuration=[
#                                   aws_ec2.SubnetConfiguration(
#                                       cidr_mask=24,
#                                       name="PublicSubnet",
#                                       subnet_type=aws_ec2.SubnetType.PUBLIC,
#                                   ),
#                                   aws_ec2.SubnetConfiguration(
#                                       cidr_mask=24,
#                                       name="PrivateSubnet",
#                                       subnet_type=aws_ec2.SubnetType.PRIVATE_WITH_EGRESS,
#                                   ),
#                                   aws_ec2.SubnetConfiguration(
#                                       cidr_mask=28,
#                                       name="IsolatedSubnet",
#                                       subnet_type=aws_ec2.SubnetType.PRIVATE_ISOLATED,
#                                   )
#                               ]
#                               )
#
#
#         # Create an EC2 instance
#         instance = aws_ec2.Instance(self, "MyInstance",
#         instance_type=aws_ec2.InstanceType("t2.micro"),
#         machine_image=aws_ec2.MachineImage.latest_amazon_linux(),
#         vpc=vpc,
#         key_name="ec2_keypair"  # Replace with your key pair name
#         )
#
