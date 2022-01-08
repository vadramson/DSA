[This was inspired from here](https://www.youtube.com/watch?v=ulprqHHWlng&t=315s)

[Install GUI Client on AWS EC2 Instance (Linux 2 and MacOS)](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-linux-2-install-gui/)

[Get an estimate of the AWS service cost by Simulating the services needed ](https://calculator.aws/#/createCalculator/EC2)


[IAM Signin link](https://vad-data.signin.aws.amazon.com/console)



**VPC** (Virtual Private Cloud): This is a virtual cloud or space within a region where we can create and lunch resources. We have more control over the security as opposed to the general cloud security. We can restrict some IP and stuff


ACL (Access Control List): Workd on a subnet level and by defualt accept all inbound and Outbound traffric unless explicitly revoked.

Security Groups are applied on EC2 instances


**Public & Private Services**

Private services(EC2, Amazon RDS, Amazone Elastic File system) exist within a VPC while Public services(S3, DynamoDB, Route 53, CloudFront) do not



# EC2 (Elastic Cloud Compute) Instances

[EC2 Instance Types](https://github.com/vadramson/DSA/blob/main/image.png)

You can use the RDP(Remote Desktop Protocol) and Remote Desktop client to connect to windows EC2 instances.

You can also use Putty client on windows to convert **.pem** keys to be able to connect to ssh from a Putty Termina


## (Identity Access management) IAM Role

IAM Role roles are used to Allows EC2 instances to call AWS services on your behalf.

