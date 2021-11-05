# [Apache Mesos](https://www.youtube.com/watch?v=51qrfr8Vu3k)
- data center kernel
- Apache Mesos is a cluster manager that provides efficient resource isolation and sharing across distributed applications or frameworks.
- The vision of mesosphere, the Company behind the project, is to create a "Datacenter Operating System" and the mesos is the kernel of it in analogy to the kernel of a normal OS.
- Program against your datacenter like it’s a single pool of resources.
- Apache Mesos abstracts CPU, memory, storage, and other compute resources away from machines (physical or virtual)
- Apache Mesos is open-source cluster manager that handles workloads efficiently in a distributed environment through dynamic resource sharing and isolation.
- Mesos is a distributed systems kernel. It is built using the same principles as the Linux kernel, only at a different level of abstraction.
- Mesos kernel runs on every machine and provides applications (e.g., Hadoop, Spark, Kafka, Elasticsearch) with API’s for resource management and scheduling across entire datacenter and cloud environments.

- Apache Mesos is a platform that allows effective resource sharing between different(Hadoop, Cassandra, Spark, Flink) applications.
- Apache Mesos helps with dynamic cluster resource allocation between applications.
- Mesos acts as an interface between machines and applications.
- It provides applications with the available resources on all machines in the cluster.
- It frequently updates this information to include resources that are freed up by applications that have reached completion status.

- you can run any distributed application, i.e. spark, Hadoop etc., that requires clustered resources.
- It sits between the application layer and the operating system and makes it easier to deploy and manage applications in large-scale clustered environments more efficiently.
- Mesos allows multiple services to scale and utilize a shared pool of servers more efficiently. The key idea behind the Mesos is to turn your data center into one very large computer.
- Apache Mesos is the opposite of virtualization because, in virtualization, one physical resource is divided into multiple virtual resources, while in Mesos, multiple physical resources are clubbed into a single virtual resource.
- Twitter, Airbnb, MediaCrossing, Xogito, and Categorize. Airbnb uses Mesos to manage their big data infrastructure.
- Mesos leverages features of modern kernels for resource isolation, prioritization, limiting, and accounting. This is normally done by cgroups in Linux or zones in Solaris.
- Mesos provides resource isolation for CPU, memory, I/O, file system, etc. It is also possible to use Linux containers but current isolation support for Linux containers in Mesos is limited to only CPU and memory.
- If you want to build a reliable platform that runs multiple mission critical workloads including Docker containers, legacy applications (e.g., Java), and distributed data services (e.g., Spark, Kafka, Cassandra, Elastic), and want all of this portable across cloud providers and/or datacenters, then Mesos (or our own Mesos distribution, Mesosphere DC/OS) is the right fit for you.

- manages computer clusters and job scheduling. It was developed at the UC Berkeley.
- Mesos is distributed systems kernel for datacenter Operating System
- Mesos uses Linux cgroups to provide isolation for CPU, memory, I/O and file system
- abstracts CPU, memory, storage, and other compute resources away from machines (physical or virtual)
- YARN is specially designed for Hadoop work loads whereas Mesos is designed for all kinds of work loads
- YARN is application level scheduler and Mesos is OS level scheduler'

# Mesos vs YARN
- Both systems have the same goal: to allow you to share a large cluster of machines between different frameworks.
- Mesos handles both memory and CPU scheduling and YARN only handles memory scheduling (i.e. you request x containers of y MB each).
- Mesos uses Linux container groups and YARN uses simple unix processes.

# Chronos
- Distributed job scheduler that supports complex job topologies. It can be used as a more fault-tolerant replacement for cron.
- Cron replacement for automatically starting and stopping services (and handling failures) that runs on top of Mesos.
- It is a distributed and fault-tolerant scheduler that runs on top of Apache Mesos that can be used for job orchestration
# [Marathon](https://mesosphere.github.io/marathon/)
- A production-grade container orchestration platform for Mesosphere’s Mesos and DC/OS.
- Marathon orchestrates both apps and frameworks.
- Provides API for starting, stopping and scaling services (and Chronos could be one of those services)
- A private PaaS built on Mesos. It automatically handles hardware or software failures and ensures that an app is "always on."
- Multiple container runtimes. Marathon has first-class support for both Mesos containers (using cgroups) and Docker.
- Stateful apps. Marathon can bind persistent storage volumes to your application. You can run databases like MySQL and Postgres, and have storage accounted for by Mesos.
# Aurora
- Aurora is a Mesos framework for long-running services and cron jobs.
- Aurora runs applications and services across a shared pool of machines, and is responsible for keeping them running, forever. When machines experience failure, Aurora intelligently reschedules those jobs onto healthy machines.

- a service scheduler that runs on top of Mesos, enabling you to run long-running services that take advantage of Mesos' scalability, fault-tolerance, and resource isolation.

