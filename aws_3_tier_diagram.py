from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2, ECS, Lambda
from diagrams.aws.database import RDS, ElastiCache, DocumentDB
from diagrams.aws.network import ALB

with Diagram("AWS 3-Tier Architecture with Redis and MongoDB", show=False):
    user = EC2("User")

    with Cluster("Presentation Layer"):
        lb = ALB("Load Balancer")

    with Cluster("Application Layer"):
        app_server = ECS("Application Server")
        lambda_function = Lambda("Lambda Function")

    with Cluster("Data Layer"):
        database = RDS("Database")
        redis_cache = ElastiCache("Redis Cache")
        mongo_db = DocumentDB("MongoDB")

    user >> lb >> app_server >> lambda_function
    lambda_function >> database
    lambda_function >> redis_cache
    lambda_function >> mongo_db