import sys

import tensorflow as tf 

cluster = tf.train.ClusterSpec({ 
  'ps': [ "192.168.2.105:8008" ],
  'worker': [ "192.168.2.108:8008", "192.168.2.145:8008"]
})

server = tf.train.Server(cluster, job_name=sys.argv[1], task_index=sys.argv[2])