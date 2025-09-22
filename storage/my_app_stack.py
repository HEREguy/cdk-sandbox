from aws_cdk import (
    Stack,
    aws_s3 as s3,
    RemovalPolicy,
    Duration
)
from constructs import Construct

class MyAppStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create an S3 bucket
        bucket = s3.Bucket(self, "sandbox_cdk_storage",
            bucket_name="sandbox-cdk-storage",  # Explicit bucket name
            versioned=True,  # Enable versioning
            encryption=s3.BucketEncryption.S3_MANAGED,  # Use S3-managed encryption
            removal_policy=RemovalPolicy.DESTROY,  # ONLY FOR TESTING - Remove this in production
            auto_delete_objects=True,  # ONLY FOR TESTING - Remove this in production
            lifecycle_rules=[
                s3.LifecycleRule(
                    expiration=Duration.days(30)  # Objects expire after 30 days
                )
            ]
        )
