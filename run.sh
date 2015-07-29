#!/bin/sh -e 

/service/get-stack-instances.py --region $REGION $STACK_OPTS | exec /service/consul-watchdog --url $CONSUL_ENPOINT $WATCHDOG_OPTS

