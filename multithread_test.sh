#! /bin/bash
instances=8

start_value=3
end_value=15000000
increment=$(( $instances * 2 ))

#debug
#echo increment: $increment
x=0
while [ $x -lt $instances ]
do
    step=$(( x * 2))
    instance_start_value=$(( start_value + $step))
#    echo instance_start_value: $instance_start_value
    python3 prime_multithread.py $instance_start_value $end_value $increment &
    x=$(( $x + 1 ))
done
wait