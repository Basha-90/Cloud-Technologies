# Containers
- OS abstraction and process isolation
- sandbox for processes, has its own namespace and c-group
- one process per container.
- portibility: container is packages with all of its dependencies
- Containers abstract applications from operating systems, much like virtualization abstracts operating systems from physical hardware.
- With block storage, you can quickly define and launch containers.
- Containers uses `Namespaces` , `C-Groups` and `Linux file System` technologies for its functions
# What process namespace and c-group?
### Namespace
- limit the process and its component visibility
### C-group
- it controles and limits the resources that a container can use
# Docker
- Build: takes docker file which consist of docker specification and turn it into docker image.
- Push: push docker image to docker registry like dockerhub
- Pull: pull docker image from docker registry
- Run: run docker image on Host OS

### Docker Image Layering
- Parent-Child heirarchical relationship between different layers of image layers
### Docker File

### Container Registry
- repository for container images like
- private or public
- Vulnerability Scanning
- RBAC-role based access control (push and pull access control)
- central user management system like LDAP/AD
- Notary to assign and verify signature of the containers images
- dockerhub: public container registry
- Harbor: an open source trusted cloud native registry project that stores, signs, and scans content

# Docker Netorking
### Default Docker Bridge
### User Defined Bridge
### Overlay Networking

# Storage
### Persistant Storage
- Volumes are stored in a part of the host filesystem managed by Docker (/var/lib/docker/volumes/ on Linux)
- These are managed by named volumes created as `docker create volumes db-data`
- These volumes are mounted as `-v db-data:/data/db` in case of mongodb.
- To persist the data, we can also mount an directory of the host system as `-v ~/.local/data/mongo:/data/db`
