# Types of Clouds
- **Private Cloud**
- **Public Cloud**
- **Community Cloud**
- **Hybrid and Multi Cloud Architecture**: Large IT organizations are increasingly looking to develop innovative software applications in hybrid and multi clouds architectures. A lot of these applications have to be developed and deployed in an on-premises private cloud for various reasons (e.g. security and compliance, data affinity, performance, etc.). This private cloud should be simple, agile, flexible, secure, cost efficient, and a key part of their overall Hybrid and Multi cloud architecture.

***
# Cloud Scalability
Cloud offerings have evolved  moved from buying units of **metal**(IaaS and PaaS) to buying **functionality**(Serverless-FaaS); or, more specifically, **throughput**. Within the AWS ecosystem that manifests itself in a database you provision by reads-and-writes(**Aurora**), a streaming system paid for in flow and an execution model bought by units-of-effort (**Lambda**).

### Vertical Scalability or Scale-up
Adding resource within the same logical unit to increase capacity. Vertical scaling can essentially resize your server with no change to your code. It is the ability to increase the capacity of existing hardware or software by adding resources. Vertical scaling is limited by the fact that you can only get as big as the size of the server. An example of this would be to add CPUs to an existing server, or expanding storage by adding hard drive on an existing RAID/SAN storage. When this is done in the cloud, **applications often get moved onto more powerful instances** and may even migrate to a different host and retire the server it was on. **Scaling-up can also be done in software by adding more threads, more connections, or in cases of database applications, increasing cache sizes**. These types of scale-up operations have been happening on-premises in datacenters for decades. However, the time it takes to procure additional recourses to scale-up a given system could take weeks or months in a traditional on-premises environment while scaling-up in the cloud can take only minutes.

### Horizontal Scalability or Scale-out
Adding multiple logical units of resources and making them work as a single unit. Most clustering solutions, distributed file systems, load-balancers help you with horizontal scalability. It is the ability to connect multiple hardware or software entities, such as servers, so that they work as a single logical unit.

Scale-out is usually associated with distributed architectures. There are two basic forms of scaling out: 
* Adding additional infrastructure capacity in pre-packaged blocks of infrastructure or nodes (i.e. hyper-converged).
* Use a distributed service that can retrieve customer information but be independent of applications or services.
 
Both approaches are used in CSPs to day along with vertical scaling for individual components (compute, memory, network, and storage) to drive down costs. Horizontal scaling makes it easy for service providers to offer “pay-as-you-grow” infrastructure and services.

### Scalability Factor
While scaling cloud resources it is import to note that every component, whether its processors, servers, storage drives or load-balancers have some kind of management/operational overhead. When you try to scale that, its important to understand what percentage of the resource is actually usable. This measurement is called **scalability factor**. If you loose 5% of a processor power every time you add a CPU to your system, then your "scalability factor" is 0.95. A scalability factor of 0.9 means you will only be able to use 90% of the resource.

Scalability can be further sub-classified based on the "scalability factor".
      
* If the scalability factor stays constant as you scale. This is called **linear scalability**.
* But chances are that some components may not scale as well as others. A scalability factor below 1.0 is called **sub-linear scalability**.
* Though rare, its possible to get better performance (scalability factor) just by adding more components (i/o across multiple disk spindles in a RAID gets better with more spindles). This is called **supra-linear scalability**.
* If the application is not designed for scalability, its possible that things can actually get worse as it scales. This is called **negative scalability**

If you need scalability, urgently, going vertical is probably going to be the easiest (provided you have the bank balance to go with it). In most cases, without a line of code change, you might be able to drop in your application on a super-expensive 64 CPU server from Sun or HP and storage from EMC, Hitachi or Netapp and everything will be fine. For a while at least. Unfortunately Vertical scaling, gets more and more expensive as you grow.

Horizontal scalability, on the other hand doesn't require you to buy more and more expensive servers. Its meant to be scaled using commodity storage and server solutions. But Horizontal scalability isn't cheap either. **The application has to be built ground up to run on multiple servers as a single application**. Two interesting problems which most application in a horizontally scalable world have to worry about are **Split brain** and **hardware failure**.


***
#  API interface 
RESTFull (Statelessness), GraphQL, Kafka, gRPC  

# [kafka](https://www.youtube.com/watch?v=aj9CDZm0Glc)  
Distributed streaming platform for real-time event-driven applications which contineously produce and consume streams of data records.

### Building Blocks
- Produce API (publish/produce)
- Consumer API (subscibe/consume)
- Topics (order list of events, can persist on disk)
- Streams API (transform the data)
- Connector API (resuable custom producers and consumers)


***
# [Object Storage](https://www.ibm.com/cloud/learn/object-storage)
- To store large amount of unstructured data in highly scalable manners
- Durability, availablility, scalability, flexibility, security
- Objects are discrete units of data that are stored in a structurally flat data environment. There are no folders, directories, or complex hierarchies as in a file-based system. Each object is a simple, self-contained repository that includes the data, metadata (descriptive information associated with an object), and a unique identifying ID number (instead of a file name and file path). This information enables an application to locate and access the object.

### Use Cases
- Disaster Recovery and Backup
- AI Analytics
- Cloud Native 
- Archive

# [Block Storage](https://www.ibm.com/cloud/learn/block-storage)
- Block storage, sometimes referred to as block-level storage, is a technology that is used to store data files on Storage Area Networks (SANs) or cloud-based storage environments. Developers favor block storage for computing situations where they require fast, efficient, and reliable data transportation.
- Block storage breaks up data into blocks and then stores those blocks as separate pieces, each with a unique identifier. The SAN places those blocks of data wherever it is most efficient. That means it can store those blocks across different systems and each block can be configured (or partitioned) to work with different operating systems.

- Block storage also decouples data from user environments, allowing that data to be spread across multiple environments. This creates multiple paths to the data and allows the user to retrieve it quickly. When a user or application requests data from a block storage system, the underlying storage system reassembles the data blocks and presents the data to the user or application.

- Block storage allows for the creation of raw storage volumes, which server-based operating systems can connect to. You can treat those raw volumes as individual hard drives. This lets you use block storage for almost any kind of application, including file storage, database storage, virtual machine file system (VMFS) volumes, and more

### Advantages
- Provides lowest possible latency
- high performance (high IOPs)
- highly redundant

# [File Storage](https://www.ibm.com/cloud/learn/file-storage)
File storage—also called file-level or file-based storage—is a hierarchical storage methodology used to organize and store data on a computer hard drive or on network-attached storage (NAS) device.  NAS or the Network Operating System (NOS) handle access rights, file sharing, file locking, and other controls. In file storage, data is stored in files, the files are organized in folders, and the folders are organized under a hierarchy of directories and subdirectories. To locate a file, all you or your computer system need is the path—from directory to subdirectory to folder to file.

# which one to choose
- Boot Volume (Block Storage)
- Workloads(Transactional or Relational Databases) that requires very low latency and high performance (Block Storage)
- Mix of structure and unstructure data (File Storage)
- Share data with many user at once (File Storage)


***
# [Data Lake](https://www.youtube.com/watch?v=LxcH6z8TFpI)
Diverse sources of data is collected by common ingestion framwork and stored in a common storage repository

***
# National Cloud Initiative
- Pakistan should develop their own cloud infrastrucure in order to compete in future tech world
# Public Research Cloud Initiative

