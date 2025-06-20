from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("AWS 3-Tier Architecture", show=False):
    elb = ELB("Load Balancer")
    web = EC2("Web Server")
    db = RDS("Database")

    elb >> web >> db