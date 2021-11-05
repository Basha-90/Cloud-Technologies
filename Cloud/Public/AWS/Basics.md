# AWS Lambda and EC2

Server-based Applications - EC2 and S3 (IaaS)  
Cloud Native Applications - AWS Lambda (Microservices, Serverless, FaaS)

EC2 requires provisioning and  management of the environment. Each EC2 instance runs not just a full copy of an operating system, but a virtual copy of all the hardware that the operating system needs to run (Virtualization).  In contrast, what AWS Lambda requires is enough system resources and dependencies to run a specific program (Containerization).


The main difference between AWS Lambda vs EC2 (virtual server-based resources) is the responsibility of provisioning. Before the emergence of agile solutions like AWS Lambda, operations teams had to allocate the resources based on the forecasting. AWS Lambda pricing is one of the biggest factors as well.


## Use Cases: When to use AWS Lambda?
When in your use case scalability is issue (due to upredictable traffic) and cost, use Lambda.
do not use Lambda when your use case required complex processing and your process can’t be executed in the limited execution time.

- Low complex code
- Shorter executing time
- Infrequent traffic
- Real-time processing
- Scheduled CRON jobs
## Use Cases: When to use EC2?
When you want to run a complex application which has consistent traffic and want to operate in a tried and tested deployment environment, EC2 if for you. The only drawbacks are a complex setup environment and provisioning of servers.

- High-performance computing
- Disaster recovery
- Easy DevOps
- Development/Testing
- Secure Environment



