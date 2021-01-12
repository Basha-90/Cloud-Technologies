# Software Defined Networking (SDN)  
## Physical Network Functions  
## NFV – Virtualized Network Functions  
## CNF - Containerized Network Functions  

Containers add a layer of abstraction, not present in VMs. While VMs rely on the infrastructure layer to provide benefits such as resilience, containers are cloud-native and are built to be independent of their infrastructure. This abstraction also enhances security, not just because patches can be rolled out faster, but because just the container host can be patched - as opposed to multiple, individual guest operating systems that each need attention. By making application development faster, scaling easier and management less complex, containers allow providers to launch newer applications (services) faster and gain a competitive advantage.

Providers aren’t converting functional VMs into containers en-masse; rather they are writing or sourcing new applications (e.g., 5G functions) as containers, while they maintain VMs with older technology that will eventually decline in number.


Container Portability: because containers are so abstracted from the infrastructure, OpenShift can run them on your cloud of choice; and move them as needed. For example, if a container is deployed in a public cloud but needs to move on premises for data locality reasons: it can.


Red Hat OpenShift Container Platform deployed in a public cloud is great but when Red Hat OpenShift is deployed on top of Red Hat OpenStack Platform, the result is an environment supporting both virtualized and containerized network functions. This allows both current and future applications to share the same infrastructure and our customers can move at their own pace by leveraging this deployment model of coexistence to migrate their VM workload or containers.
