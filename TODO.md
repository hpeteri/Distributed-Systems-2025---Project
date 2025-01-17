# Week 1

- Basic Client/Server implementation for video streaming

## client

REST API for retrieving a single video from database

**GET**  

for now the request can be empty. API will later change anyways, so there is no point to add request body.

## vid_cache

Upon **GET** request from client. Request video file from vid_raw service.

Upon receiving file from vid_raw service. Store local copy to cache.

## vid_raw

Video files can be inside the directory tree. At somepoint add database for tree traversal, but for now serve only 1 video.

Upon **GET**(what ever the right term is for gRPC)  request from vid_cache. Respond with video file. [gRPC]
