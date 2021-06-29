import datetime
from rediscluster import RedisCluster


redisPassword = "stupidpass"
redisClusterNodes = [{"host": "127.0.0.1", "port": "7001"}, {"host": "127.0.0.1", "port": "7002"}, 
					 {"host": "127.0.0.1", "port": "7003"}, {"host": "127.0.0.1", "port": "7004"}, 
					 {"host": "127.0.0.1", "port": "7005"}, {"host": "127.0.0.1", "port": "7006"}]

def lambda_handler(event, context):

	timestamp = datetime.datetime.utcnow().isoformat() + 'Z';
	
	try:
		redisCluster = RedisCluster(startup_nodes=redisClusterNodes, decode_responses=True, skip_full_coverage_check=True, password=redisPassword);
		emails = redisCluster.keys();  #keys = <class 'list'>
	except Exception as e:
		print("[Error] Failed to connect to redis : {}".format(e));
		return {
			"code" : "0005",
			"desc" : "Failed to connect to redis",
			"timestamp" : timestamp
		}

	return {
		"code" : "0",
		"desc" : "success",
		"timestamp" : timestamp,
		"data" : {
			"emails" : emails
		}
	}
