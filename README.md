## Usage

    usage: consul-watchdog [-h] [--url URL] [--status STATUS] [--input INPUT]
                           [--debug]

                           Cleans up members of a Consul Cluster.

                           optional arguments:
                           -h, --help       show this help message and exit
                           --url URL        Consul Members Endpoint
                           --status STATUS  Consul Member Status for eviction
                           --input INPUT    File with valid hosts, without list is read from stdin
                           --debug          Debug information output





Example : 

     python get-stack-instances.py --region eu-west-1 --location prod-eu-west-1 --envid a | python consul-watchdog


or : 
    echo 10.11.68.52 10.11.43.107 | python consul-watchdog --debug
    Valid: 2
    Failed: 6
    Missing: 5
    Removed 10.11.32.104
    Removed 10.11.41.246
    Removed 10.11.72.45


