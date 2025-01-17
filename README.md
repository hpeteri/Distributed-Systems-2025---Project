This is a repository for Distributed Systems 2025 project

Group 33:

Group Members
- Henrik Peteri  
- Aleksanteri Seppä  

# Project Topic - 2. Telco-Edge CDN for Latency-Sensitive Video Streaming
## 6-Week outline

1. Introduction: Basic client-server for video streaming.  
2. Communication: Implement edge–core communication for content requests and updates.  
3. Time & Consensus: Maintain consistent cache indices across edge nodes via consensus.  
4. Performance & Scalability: Introduce load balancing between edge nodes to handle high streaming demands.  
5. Replication & Consistency: Replicate streaming segments with eventual consistency for quick cache updates.  
6. Resource Scheduling: Allocate edge cache capacity based on content popularity.  
7. System Architecture: Separate streaming controller (microservice), caching logic (microservice), and client request handler.  
8. Middleware: Logging and analytics middleware to track popular content, QoS metrics, and user sessions.  
9. Datacenter & Cloud: Deploy in a telco datacenter environment with simulated network topologies.  
10. Big Data Processing:  Process logs in a batch job to extract content popularity patterns.  
11. Distributed ML:  Predict video demand spikes in near-real-time using a distributed ML model across edge nodes.  
12. Edge–Cloud Continuum: Seamlessly offload large-scale content pre-caching to the cloud while local streams stay at the edge.  


# Architecture

## client / 

**responsibilies:**  
- retrieve video metadata from vid_metadata service [REST]  
- hosts web page for viewing video  

## vid_cache_broker

Load balancer for numerous vid_cache services

## vid_cache

Local database for raw video files to reduce latency

**Responsibilities:**  
- cache raw video files

## vid_metadata

Video metadata database

medata includes:  
video name, tag, filetype, length  

**Responsibilities:**  
- serve video metadata to client

## vid_raw

Video Databse for raw files

**Responsibilities:**  
- serve video files to vid_cache [Fast api, gRPC]

**Service requirements:**  
- async or sync transmission
