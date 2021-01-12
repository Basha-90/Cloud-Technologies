# Virtualization
- It is hardware level abstraction. 
- Machines (OS isolation).
- Hardware level access. 
- Infinite flexibility of hardware.
It is abstraction of physical IT ressources (Compute, RAM, Storage, Networking). It is heavy weight as compared to container.
### Hyperviser
A hypervisor is software that creates and runs virtual machines (VMs).
#### Type 1 Hyperviser
A type 1 hypervisor, also referred to as a native or bare metal hypervisor, runs directly on the host’s hardware to manage guest operating systems. It takes the place of a host operating system and VM resources are scheduled directly to the hardware by the hypervisor. This type of hypervisor is most common in an enterprise data center or other server-based environments.

KVM, Microsoft Hyper-V, and VMware vSphere are examples of a type 1 hypervisor. KVM was merged into the Linux kernel in 2007, so if you’re using a modern version of Linux, you already have access to KVM. 

#### Type 2 Hyperviser
A type 2 hypervisor is also known as a hosted hypervisor, and is run on a conventional operating system as a software layer or application.
It works by abstracting guest operating systems from the host operating system. VM resources are scheduled against a host operating system, which is then executed against the hardware. A type 2 hypervisor is better for individual users who want to run multiple operating systems on a personal computer. 

VMware Workstation and Oracle VirtualBox are examples of a type 2 hypervisor. 

#### Hyperconvergence
Hyperconvergence is an IT framework that combines storage, computing and networking into a single system in an effort to reduce data center complexity and increase scalability. Hyperconverged platforms include a hypervisor for virtualized computing, software-defined storage, and virtualized networking. Hyper-converged infrastructure has become increasingly popular for use in private cloud and this approach is not quite as loosely coupled as other forms of distributed architectures.

***
# Container
- It is OS level abstraction. 
- Process isolation. 
- Container uses two features of linux kernel (**namespaces(which helps each container instance has its own OS(process isolation)) and cgroup(monitoring and metering of resources)**)to create ilusion of isolation of processes. 
- Infinite portability.
- Application code is packaged, along with its libraries and dependencies.
- Containers are small, fast, and portable because unlike a virtual machine, containers do not need include a guest OS in every instance and can, instead, simply leverage the features and resources of the host OS.
- **The underlying infrastructure for containerization is less relevant**

### Use cases of containers
- Microservices
- DevOps
- Hybrid, multi-cloud
- Application modernizing and migration

### Container orchestration with Kubernetes 
Kubernetes enables developers and operators to declare a desired state of their overall container environment through YAML files, and then Kubernetes does all the hard work establishing and maintaining that state, with activities that include deploying a specified number of instances of a given application or workload, rebooting that application if it fails, load balancing, auto-scaling, zero downtime deployments and more.

### Tools in containers ecosystem 
- Docker (Containerization Platform)
- K8s (Container Orchestration Platforms)
- Docker Swarm (Container Orchestration Platforms)
- Nomad (Container Orchestration Platforms)
- Apache Mesos (Container Orchestration Platforms)
- [Istio](https://www.ibm.com/cloud/learn/istio) (For Sevice Mesh) : API Gateway to manage, and secure networks of different microservices in K8s.
- [Knative](https://www.ibm.com/cloud/learn/knative) (FaaS) : It helps to offer container services as serverless functions on top of K8s.

### Containers vs VMs
Containers and VMs both create abstraction and isolation of computing enviroment.

Red Hat OpenShift Container Platform (CaaS, PaaS)
Red Hat OpenStack VM Platform (IaaS)

### Red Hat OpenShift or Red Hat OpenStack Platform: When to use What and Why?
#### The Virtualization Revolution
**Red Hat OpenStack** is an **virtualization plateform** which offer **IaaS platform** (native VMs) and **Bare Metal as a Service** for high performance applications. **Natively, Red Hat OpenStack Platform runs VMs and bare metal, but when paired with Red Hat OpenShift, it can also handle containers.**
#### The Container Evolution
**Red Hat OpenShift** is a **containerization platform** which run containerized applications run on the infrastructure.

