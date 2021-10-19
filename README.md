# callAPIGWfromLamba
Lambda call private APIGW in different region within VPC
record the time consumed for latency test

Step1: setup APIGW and vpce in HK region

refer to https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html



1.1 VPC setup

use default VPC or setup a new VPC

1.2 VPCE setup

Create VPCE
VPCE: 
vpce-07axxxxxxxa5f 
com.amazonaws.ap-east-1.execute-api 
172.31.17.71 172.31.9.85 172.31.44.113

For Security group, select the security group to associate with the VPC endpoint network interfaces.
The security group you choose must be set to allow TCP Port 443 inbound HTTPS traffic from either an IP range in your VPC or another security group in your VPC.


1.3 APIGW setup

refer to https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-from-example.html

setup a sample APIGW for petstore.
associate the vpce with vpce-07ab213eeb77f4a5f 
config the resource policy to allow the access
deploy the APGW, 
Test apgw from console, run apigw test post, get methold

default endpoint  https://xxxxxxxxx.execute-api.ap-east-1.amazonaws.com (https://xxxxxxx.execute-api.ap-east-1.amazonaws.com/)


1.4 test from local VPC via VPCE

*#login to bastion server*

ssh -i "key4hk.pem" ec2-user@ec2-xxxxx.ap-east-1.compute.amazonaws.com


*#call the apigw from vpce*
https://{rest-api-id}-{vpce-id}.execute-api.{region}.amazonaws.com/{stage (https://{rest-api-id}-{vpce-id}.execute-api.{region}.amazonaws.com/%7Bstage)}
curl -v https://xxxxxxx-vpce-xxxxxxxxxx.execute-api.ap-east-1.amazonaws.com/test/pets?1


Step2 TGW setup in HK & Tokyo region


Create TGW in HK region, tgw-0b6681fe08da8f9e8
Create TGW attahchment for HK VPC
[Image: Screen Shot 2021-08-06 at 3.41.46 PM.png]
Create TGW in Tokyo region
Create TGW attahchment for HK VPC

[Image: Screen Shot 2021-08-06 at 3.38.09 PM.png]
HK region: Create TGW peer from HK region with Tokyo region
Tokyo region: accept peering request from HK region

HK region:
VPC route table update
TGW route update

Tokyo region
VPC route table update
TGW route update
[Image: Screen Shot 2021-08-06 at 3.39.29 PM.png]
Step3 Lambda setup in Tokyo region

lambda: lambda-cognito-test
Role: add ec2 full access right
vpc:
subnet:

lambda python 3.7


python 3.7

Role: add ec2 full access right

need subnet and VPC for lambda

Test log@SG

Test Event Name

hello



Response

"value1"



Function Logs

START RequestId: 1da3fda5-0add-43e0-a42b-570c4b384f47 Version: $LATEST

END RequestId: 1da3fda5-0add-43e0-a42b-570c4b384f47

REPORT RequestId: 1da3fda5-0add-43e0-a42b-570c4b384f47 Duration: 22787.43 ms Billed Duration: 22788 ms Memory Size: 128 MB Max Memory Used: 58 MB Init Duration: 208.44 ms


Request ID
1da3fda5-0add-43e0-a42b-570c4b384f47
