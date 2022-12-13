# install-confluent-platform
Simple repository with Dockerfile for installing Confluent Platform tools in a container


## Build process

To build the docker image locally you can do so via the following command

``` Example for version 7.2.2
docker build --build-arg CONFLUENT_URL=http://packages.confluent.io/archive --build-arg CONFLUENT_MAJOR_VERSION=7.2 --build-arg CONFLUENT_MINOR_VERSION=7.2.2 --build-arg INSTALL_DIR=/tmp -t cp-tools .
```