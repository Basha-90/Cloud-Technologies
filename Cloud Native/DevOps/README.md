# Agile
- Agile is an iterative approach to project management and software product development
- It helps teams deliver value to their customers faster and with fewer headaches.
- Requirements, plans, and results are evaluated continuously so teams have a natural mechanism for responding to change quickly.
- It recognizes the volatility of product development, and provides a methodology for self-organizing teams to respond to change without going off the rails
# Scrum vs Kanban
- different strategies for implementing an agile development or project management system
- different methodologies for managing complex work.
### Scrum
- A structured agile approach.
- Short and structured work sprint.
- To ship working software through set intervals called sprints
- Deliver value to customer(add bussiness value) after each sprint
### Kanban
- continuous and more fluid
- visualizing work(workflow)

### Jira
- A tools for agile paractices
***

# Enterprise Software Solution Architecture
- [Martin Fowler – What Does Tech Excellence Look Like? | TW Live Australia 2016](https://www.youtube.com/watch?v=Avs70dZ3Vlk)  
- Design Patterns  
- ["Agile Architecture" - Molly Dishman & Martin Fowler Keynote](https://www.youtube.com/watch?v=VjKYO6DP3fo)
- [Architecture](https://martinfowler.com/architecture/)

***
# Agile Software Development
**Agile software development requires adaptive planning, evolutionary development, and delivery.**  
Continuous software delivery which enables customers to seize market opportunities and reduce time to customer feedback. Agile enables developers to deliver their functions every two weeks to respond to changing business needs. DevOps focuses on the operational side of the software development lifecycle, reducing handoffs from developer to operations teams, reducing the time to testing and deploying code, and decreasing errors and downtime of operational systems.


Many software development methodologies, frameworks, and practices fall under the umbrella of being agile, including:
- Scrum
- Kanban (visual workflow)
- XP (eXtreme Programming)
- Lean
- DevOps

All of these have been used on their own or in combination for developing and deploying software. The most common are scrum, kanban (or the combination called scrumban), and DevOps.

Scrum is a framework under which a team, generally consisting of a scrum master, product owner, and developers, operates cross-functionally and in a self-directed manner to increase the speed of software delivery and to bring greater business value to the customer. The focus is on faster iterations with smaller increments.

Kanban is an agile framework, sometimes called a workflow management system, that helps teams visualize their work and maximize efficiency (thus being agile). Kanban is usually represented by a digital or physical board. A team's work moves across the board, for example, from not started, to in progress, testing, and finished, as it progresses. Kanban allows each team member to see the state of all work at any time.

The difference between the two is what happens after development.  

Software development, testing, and deployment happen in both DevOps and agile. However, pure agile tends to stop after these three stages. In contrast, DevOps includes operations, which happen continually. Therefore, monitoring and software development are also continuous.

## Resources 
[Martin Fowler – Agile Essence and Fluency](https://www.youtube.com/watch?v=URlnxbaHhTs)  


***
# DevOps
Evolution of Agile software development and delivery. To automate and integrate the processes between software development and operations teams.
## Continuous Integration
**Code Centric.** 
**To frequently code, build, integrate, and test (to reduce merge hell)**  
A software development and DevOps practice where each developer integrates their work with the main branch of code at least once a day in order to identify integration issues earlier, when they are easier to fix.

## Continuous Delivery
**Release Centric.** 
DevOps practice that focuses on delivering any validated changes to code—updates, bug fixes, even new features—to users as quickly and safely as possible. Continuous delivery picks up where continuous integration ends, automating the delivery of applications to selected infrastructure environments. It ensures automated pushing of code changes to different environments, such as development, testing, and production.

### Resources
- [Martin Fowler – Continuous Delivery](https://www.youtube.com/watch?v=aoMfbgF2D_4)  
- [Contineous Delivery 101](https://www.youtube.com/playlist?list=PLYcy44QqzleK37bEsG5Jh9RQDmUaBoMra)  
- [Contineous Delivery](https://www.youtube.com/playlist?list=PLYcy44QqzleJervy1ajJcad_CsgJr7ZJw)  


## Continuous Deployment
**Deployment Centric.** 
**Which focuses on automating releases of projects as soon as possible.**
Continuous deployment is a strategy in software development where code changes to an application are released automatically into the production environment. Continuous delivery is the automated movement of code through the development lifecycle (sometimes called the delivery lifecycle); continuous deployment is the automated movement of that code into production, once it passes the required automated tests.


# CI/CD Pipeline Tool Chain

0. Planning : Jira (Scrum, Kanban)
1. Version Control : Git
2. Orchestration (manage the process end-2-end and define the stages in pipelines) : Jenkins, Travis CI, Bamboo, CircleCI, gitlab, Team City
3. Configration Management/Infrastructure Automation : Cheff, Puppet, Ansible
4. Testing : Selenium, JUnit, Appium, Jmeter, Zephyr
5. Deployment Tools (for Installing Application) : Capistrano, CA Nolio, Rapid Deploy, MDT, Octopus
6. Containers : Dockers, Kubernetes, rkt
7. Continuous Monitoring : Nagios, Prometheus, Zabbix, Icinga, Sensu, SysDig
 
## DevSecOps
 
## Books
- Continuous Delivery by David Farley and Jez Humble
## Tekton
Kubernetes-native CI/CD building blocks. It lets you build, test, and deploy across multiple cloud providers or on-premises systems by abstracting away the underlying implementation details.

