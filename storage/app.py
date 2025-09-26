#!/usr/bin/env python3
from aws_cdk import App, Environment
from my_app_stack import MyAppStack

app = App()
MyAppStack(app, "MyAppStack",
           env=Environment(account=app.account, region=app.region))

app.synth()
