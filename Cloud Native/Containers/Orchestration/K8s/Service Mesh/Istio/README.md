# What is Istio?
- Service Mesh solution
- Service Mesh: a way to connect all the microservices to one consistance network and observability layer
- It abstract networking away from application
### Architecture
- Galley: config validation and distribution
- Pilot: understand the topology of service mesh and programming envoy proxy sidecar
- Citadel: issue identity to applications and behaves as Certificate Authority(CA)
- Mixer: applying policy and generating telemetry data

### Key Feature
- Traffic Management
- Visibility
- Security
- Consistancy and Centrality
