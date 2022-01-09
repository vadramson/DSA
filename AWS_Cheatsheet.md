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

IAM Role roles are used to Allows EC2 instances to call AWS services on your behalf. (This is a very secure way as the connection credentials are frequently regenerated) 


## Auto-Scaling EC2 instances
[Auto-Scaling EC2 instances](https://github.com/vadramson/DSA/blob/main/Auto-Scaling-EC2.png) can launch out EC2 instances if more compute power is needed or can reduce running instances if less compute power is need.

This is done automatically and it helps reduce cost



# Connecting to Ubuntu EC2 instance from local desktop

**Step 1:**

SSH into the remote EC2 terminal and 

    sudo apt update

Install xrdp to allow RDP connections:

    sudo apt install ubuntu-desktop
    sudo apt install xrdp

Set a password for the ubuntu user:

    sudo passwd your_desired_pwd

**Step 2:**

Go to AWS console (EC2 Dashboard)

Click on Instances(running)

Select your running Ubuntu instance

Go to Security

Click on Security Groups

Click on Edit inbound rules

In type drop down select RDP

It by default select port 3389

In Source add 0.0.0.0/0 IP

Click on Save rules

**Step 3:**

Open Remote Desktop Connection on your local machine

Enter Computer: Public IPv4 DNS of Ubuntu ec2 and add username:your_user_name (most common __ec2-user__)

click on connect will open up GUI version of Ubuntu (linux), It ask for password please enter the set password.



