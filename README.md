Commands to run (within downloaded repo):

~~~docker build -t cloud-docker-hw .
~~~
Then (for default files already included in image):
~~~
docker run cloud-docker-hw
~~~
Or (if supplying a specific volume or input file):
~~~
docker run -v $pwd/[Directory containing input files]/:/cloud-docker/home/data cloud-docker-hw
~~~


