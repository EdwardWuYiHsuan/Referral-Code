import datetime
from rediscluster import RedisCluster


redisPassword = "stupidpass"
redisClusterNodes = [{"host": "127.0.0.1", "port": "7001"}, {"host": "127.0.0.1", "port": "7002"}, 
					 {"host": "127.0.0.1", "port": "7003"}, {"host": "127.0.0.1", "port": "7004"}, 
					 {"host": "127.0.0.1", "port": "7005"}, {"host": "127.0.0.1", "port": "7006"}]

def lambda_handler(event, context):
	
	print("[Info] Request : {}".format(event));
	timestamp = datetime.datetime.utcnow().isoformat() + 'Z';
	
	email = event.get("email");
	if email is None:
		return {
			"code": "0001",
			"desc" : "Invalid 'email'",
			"timestamp" : timestamp
		}
	
	referralCode = event.get("referral_code");
	if referralCode is None:
		return {
			"code": "0002",
			"desc" : "Invalid 'referral_code'",
			"timestamp" : timestamp
		}
	
	try:
		redisCluster = RedisCluster(startup_nodes=redisClusterNodes, decode_responses=True, skip_full_coverage_check=True, password=redisPassword);
		result = redisCluster.set(email, referralCode);  # type is boolean
	except Exception as e:
		print("[Error] Failed to connect to redis : {}".format(e));
		return {
			"code" : "0005",
			"desc" : "Failed to connect to redis",
			"timestamp" : timestamp
		}
	
	print("[Info] Push data result : {}".format(result));
	if not result:
		return {
			"code": "0003",
			"desc" : "Failed to push data",
			"timestamp" : timestamp
		}

	return {
		"code": "0",
		"desc" : "success",
		"timestamp" : timestamp
	}
