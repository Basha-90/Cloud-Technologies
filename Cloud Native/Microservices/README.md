# Microservices Architecture
Microservices architecture is an approach(cloud native) in which a single application is composed of many loosely coupled and independently deployable smaller services. These services are language and framework independant.

### Key enabling technologies and tools

- Microservices both enable, and require, DevOps
- Containers, Docker, and Kubernetes
- API gateways : Ingress, Istio
- Messaging : Apache Kafka
- Serverless : Serverless Architectures and Functions-as-a-Service (FaaS) platforms share affinity with microservices

#### Service Mesh
A service mesh, like the open source project **Istio**, is a way to control how different parts of an application share data with one another. a service mesh is a dedicated infrastructure layer built right into an app. This visible infrastructure layer can document how well (or not) different parts of an app interact, so it becomes easier to optimize communication and avoid downtime as an app grows. service mesh takes the logic governing service-to-service communication out of individual services and abstracts it to a layer of infrastructure. a service mesh is built into an app as an array of network proxies. 

In a service mesh, requests are routed between microservices through proxies in their own infrastructure layer. For this reason, individual proxies that make up a service mesh are sometimes called “sidecars,” since they run alongside each service, rather than within them. Taken together, these “sidecar” proxies—decoupled from each service—form a mesh network. A sidecar proxy sits alongside a microservice and routes requests to other proxies. Together, these sidecars form a mesh network.  service mesh also captures every aspect of service-to-service communication as performance metrics. Over time, data made visible by the service mesh can be applied to the rules for interservice communication, resulting in more efficient and reliable service requests.


Distributed tracing of requests through Jaeger presents a visible infrastructure layer alongside services, so problems are easier to recognize and diagnose. Jaeger is open source software for tracing transactions between distributed services. Distributed tracing is a way to see and understand the whole chain of events in a complex interaction between microservices. It’s used for monitoring and troubleshooting complex microservices environments. It’s often run as part of a service mesh, which is a way to manage and observe microservices.


### Common patterns
- Backend-for-frontend (BFF) pattern
- Entity and aggregate patterns
- Service discovery patterns
- Adapter microservices patterns
- Strangler application pattern

### Anti-patterns
- The first rule of microservices is, don’t build microservices : don’t start with microservices. Microservices are a way to manage complexity once applications have gotten too large and unwieldly to be updated and maintained easily.
- Don’t do microservices without DevOps or cloud service
- Don’t make too many microservices by making them too small
- Don’t turn microservices into SOA
- Don’t try to be Netflix

### Resources
[Migration to a Microservices Ecosystem with Martin Fowler](https://www.youtube.com/watch?v=6-vNG33En88)  
[Good Introduction to Microservices by Martin Fowler](https://www.youtube.com/watch?v=wgdBVIX9ifA)  
[microservices](https://martinfowler.com/microservices/)  
[Microservices](https://martinfowler.com/articles/microservices.html)  
[Martin Fowler – Microservices](https://www.youtube.com/watch?v=2yko4TbC8cI)  
[GOTO 2020 • When To Use Microservices (And When Not To!) • Sam Newman & Martin Fowler](https://www.youtube.com/watch?v=GBTdnfD6s5Q)  
[GOTO Conferences](https://www.youtube.com/channel/UCs_tLP3AiwYKwdUHpltJPuA)


***
# Stateless or Stateful Services
Whether something is stateful or stateless depends on how long the state of interaction with it is being recorded and how that information needs to be stored. 

The loosely coupled nature of the cloud means apps are not tied to infrastructure, which means they are stateless. A cloud native app stores its state in a database or some other external entity so instances can come and go and the app can still track where in the unit of work the application is. “This is the essence of loosely coupled. Not being tied to infrastructure allows and app to run in a highly distributed manner and still maintain its state independent of the elastic nature of the underlying infrastructure,” Kavis says.

Most on-premises apps are stateful, meaning they store the state of the app on the infrastructure the code runs on. The app can be broken when adding server resources because of this.
## Stateless
**No cache or database.**  
**Good for horizontal scalability.**  
There is no stored knowledge of or reference to past transactions. Each transaction is made as if from scratch for the first time.

An example of a stateless transaction would be doing a search online to answer a question you’ve thought of. You type your question into a search engine and hit enter. If your transaction is interrupted or closed accidentally, you just start a new one. Think of stateless transactions as a vending machine: a single request and a response. 

## Stateful
Stateful applications and processes, however, are those that can be returned to again and again, like online banking or email. They’re performed with the context of previous transactions and the current transaction may be affected by what happened during previous transactions. For these reasons, **stateful apps use the same servers each time they process a request from a user.**  

If a stateful transaction is interrupted, the context and history have been stored so you can more or less pick up where you left off. Stateful apps track things like window location, setting preferences, and recent activity. You can think of stateful transactions as an ongoing periodic conversation with the same person.

##### Containers and state
**Originally, containers were built to be stateless, as this suited their portable, flexible nature.** But as containers have come into more widespread use, people began containerizing (redesigning and repackaging for the purposes of running from containers) existing stateful apps. This gave them the flexibility and speed of using containers, but with the storage and context of statefulness. Because of this, stateful applications can look a lot like stateless ones and vice versa. For example, you might have an app that is stateless, requiring no long-term storage, but that allows the server to track requests originating from the same client by using cookies.

We used data storage, Kubernetes, and StatefulSets to manage both stateless and stateful containers.

## Resources 
[Stateful vs. Stateless: the good, the bad and the ugly](https://medium.com/proud2becloud/stateful-vs-stateless-the-good-the-bad-and-the-ugly-1930948a3755)  
[Cloud Native Applications: Stateless or Stateful Services?](https://thenewstack.io/cloud-native-applications-stateless-or-stateful-services/)  
[Stateful and Stateless Applications](https://www.xenonstack.com/insights/stateful-and-stateless-applications/)
