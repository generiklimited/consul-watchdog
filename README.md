# About

hashicorp consul is amazing, but its default handling of failed nodes is appalling.
This script takes a list of valid nodes ( space separated ).
Compares the failed ones from consul to list of valid nodes and issues force-leave command only to the ones which are not valid.

We generate the list of valid nodes from AWS instances and feed it on stdin to watchdog as per example.


## Usage

   usage: consul-watchdog [-h] [--url URL] [--status STATUS] [--input INPUT] [--debug] [--dryrun]

              Cleans up members of a Consul Cluster.

              optional arguments:
              -h, --help       show this help message and exit
              --url URL        Consul Members Endpoint
              --status STATUS  Consul Member Status for eviction
              --input INPUT    File with valid hosts, without list is read from stdin
              --debug          Debug information output
              --dryrun         Do not remove the nodes, just pretend






Example : 

     python get-stack-instances.py --region eu-west-1 | python consul-watchdog --dryrun --debug


or : 

    echo 10.11.68.52 10.11.43.107 | python consul-watchdog --debug --dryrun
    Valid: 2
    Failed: 6
    Missing: 5
    Removed 10.11.32.104
    Removed 10.11.41.246
    Removed 10.11.72.45


The container is only doing dryrun by default with ```ENV WATCHDOG_OPTS "--dryrun --debug"``` , you need to reset it to other value when runing for example : 

   docker run -e WATCHDOG_OPTS='--debug' consul-watchdog
