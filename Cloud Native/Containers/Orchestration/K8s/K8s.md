# K8s
## Resources
- [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/)
- [What is Kubernetes? Red Hat](https://www.redhat.com/en/topics/containers/what-is-kubernetes)
- [Kubernetes Essentials IBM](https://www.youtube.com/playlist?list=PLOspHqNVtKABAVX4azqPIu6UfsPzSu2YN)
- [kubernetes IBM](https://www.ibm.com/cloud/learn/kubernetes?)
- [kubernetes tutorials IBM](https://www.ibm.com/cloud/container-service/kubernetes-tutorials)

# etcd
- A distributed, reliable key-value store for the most critical data of a distributed system.
- It is core component of K8s and others distributed systems.
- It manages the configuration data, state data, and metadata for Kubernetes.

# [Knative](https://www.ibm.com/cloud/learn/knative)
- It provides FaaS 
- It helps to offer container services as serverless functions on top of K8s.
# [Istio](https://www.ibm.com/cloud/learn/istio) 
- For Sevice Mesh
- API Gateway to manage, and secure networks of different microservices in K8s.
# Tekton
Kubernetes-native CI/CD building blocks. It lets you build, test, and deploy across multiple cloud providers or on-premises systems by abstracting away the underlying implementation details.

# OpenShift
- Red Hat OpenShift is an enterprise-ready Kubernetes container platform with full-stack automated operations to manage hybrid cloud and multicloud deployments. 
- Red Hat OpenShift is optimized to improve developer productivity and promote innovation.
- Red Hat OpenShift is an open source container application platform that also incorporates a collection of software that gives you the ability to run an entire Kubernetes environment.
- Different [flavours](https://www.openshift.com/products) are available of OpenShift(OpenShift Container Platform, OKD, OpenShift Online, OpenShift Dedicated)
- OKD-Origin Community Distribution (The Community Distribution of Kubernetes that powers Red Hat's OpenShift)

# Consul
- Consul is a service networking solution for distributed systems, the capabilities of which sit somewhere between those of etcd and the Istio service mesh for Kubernetes. 

# Redis
- Like etcd, Redis is an open source tool, but their basic functionalities are different.
- Redis is an in-memory data store and can function as a database, cache, or message broker. Redis supports a wider variety of data types and structures than etcd and has much faster read/write performance.
- But etcd has superior fault tolerance, stronger failover and continuous data availability capabilities, and, most importantly, etcd persists all stored data to disk, essentially sacrificing speed for greater reliability and guaranteed consistency.
- For these reasons, Redis is better suited for serving as a distributed memory caching system than for storing and distributed system configuration information.

# Nomads
- Nomad is a flexible workload orchestrator that enables an organization to easily deploy and manage any containerized or legacy application using a single, unified workflow.
- Nomad can run a diverse workload of Docker, non-containerized, microservice, and batch applications.
- Nomad enables developers to use declarative infrastructure-as-code for deploying applications. Nomad uses bin packing to efficiently schedule jobs and optimize for resource utilization.
- In one Nomad cluster, you can run Docker containers, VMs, and Java JARs—as an example. Kubernetes, on the other hand, is mostly built for containers only.

# Apache Mesos
-  Apache Mesos is open-source cluster manager that handles workloads efficiently in a distributed environment through dynamic resource sharing and isolation.
- you can run any distributed application, i.e. spark, Hadoop etc., that requires clustered resources.
- It sits between the application layer and the operating system and makes it easier to deploy and manage applications in large-scale clustered environments more efficiently.
- Mesos allows multiple services to scale and utilize a shared pool of servers more efficiently. The key idea behind the Mesos is to turn your data center into one very large computer.
- Apache Mesos is the opposite of virtualization because, in virtualization, one physical resource is divided into multiple virtual resources, while in Mesos, multiple physical resources are clubbed into a single virtual resource.
- Twitter, Airbnb, MediaCrossing, Xogito, and Categorize. Airbnb uses Mesos to manage their big data infrastructure.
- Mesos leverages features of modern kernels for resource isolation, prioritization, limiting, and accounting. This is normally done by cgroups in Linux or zones in Solaris.
- Mesos provides resource isolation for CPU, memory, I/O, file system, etc. It is also possible to use Linux containers but current isolation support for Linux containers in Mesos is limited to only CPU and memory.
