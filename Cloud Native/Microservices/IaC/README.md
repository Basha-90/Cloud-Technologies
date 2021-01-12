# Infrastructure as Code (IaC)-Cloud Provisioning Automation
Cloud Provisioning is the process of setting up Cloud Infrastructure. Today, **Cloud infrastructure** is often **defined in software**, and **virtualization** and **containers** have sped up the provisioning process while eliminating the need for frequent hardware provisioning and management. **Infrastructure as Code (IaC)** automates the provisioning, configration, management  of cloud infrastructure. **IaC** is the provisioning, configration, mantainance and managing of cloud infrastructure through code instead of through manual processes. With IaC, you **defines infrastructure(infrastructure specifications)** in **configuration files**. In IaC infrastructure takes a modular approach.  

**IaC** is also an essential **DevOps** practice, indispensable to a competitively paced software delivery lifecycle. It enables DevOps teams to rapidly create and version infrastructure in the same way they version source code and to track these versions so as to avoid inconsistency among IT environments (**environment drift** and  **configuration drift**) that can lead to serious issues during deployment.

## Immutable infrastructure vs. mutable infrastructure

**Mutable Infrastructure** is the infrastructure that can be modified or updated after it is originally provisioned. Mutable infrastructure gives development teams the flexibility to make ad hoc server customizations to, say, more closely fit development or application requirements or respond to an emergent security issue. But, it also undermines a key IaC benefit—the ability to maintain consistency between deployments or within versions—and can make infrastructure version tracking much more difficult.

**Immutable Infrastructure** is the infrastructure that cannot be modified once originally provisioned. If immutable infrastructure needs to be changed, it has to be replaced with new infrastructure. Because new infrastructure can be spun up quickly on the cloud—particularly with IaC—immutable infrastructure is much more feasible and practical than it sounds.

Immutable infrastructure takes IaC to a next logical step, essentially hardening IaC to further ensure the benefits it offers. It all but eliminates configuration drift and makes it even easier to maintain consistency between test and deployment environment. It also makes it easier to maintain and track infrastructure versions and to confidently roll back to any version when necessary.

## Declarative vs. imperative approach

In the **declarative approach** know as **functional approach**, you specify the desired final state of the infrastructure you want to provision and the IaC software handles the rest—spinning up the virtual machine (VM) or container, installing and configuring the necessary software, resolving system and software interdependencies, and managing versioning. The chief downside of the declarative approach is that it typically requires a skilled administrator to set up and manage, and these administrators often specialize in their preferred solution.

In the **imperative approach** also known as the **procedural approach** you prepare automation scripts that provision your infrastructure one specific step at a time. While this can be more work to manage as you scale, it can be easier for existing administrative staff to understand and can leverage configuration scripts you already have in place.

## [Infrastructure as Code tools](https://www.ibm.com/cloud/blog/chef-ansible-puppet-terraform)

### Ansible
**Ansible**  automate **provisioning, configuration management, and application deployment** of cloud infrasturture for an enterprise. A **declarative** automation tool, Ansible lets you create ‘playbooks’ (written in the YAML configuration language) to specify the desired state for your infrastructure and then does the provisioning for you. Ansible is a popular choice for automating provisioning of Docker containers and Kubernetes deployments.

### Terraform

Terraform is another declarative provisioning and infrastructure orchestration tool that lets engineers automate provisioning of all aspects of their enterprise cloud-based and on-premises infrastructure.

Terraform works with all the leading cloud providers and lets you automate the build-out of resources across multiple providers in parallel, regardless of where physical servers, DNS servers, or databases reside. It can also provision applications written in any language.

Unlike Ansible, Terraform does not offer configuration management capabilities, but it works hand-in-hand with configuration management tools (e.g., Cloud Formation) to automatically provision infrastructure in the state described by configuration files and to automatically change update provisioning when necessary in response to configuration changes.

### Chef
### Puppet
