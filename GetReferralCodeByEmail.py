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
			"code" : "79001",
			"desc" : "Invalid 'email'",
			"timestamp" : timestamp
		}

	try:
		redisCluster = RedisCluster(startup_nodes=redisClusterNodes, decode_responses=True, skip_full_coverage_check=True, password=redisPassword);
		referralCode = redisCluster.get(email);
		if referralCode is None:
			return {
				"code" : "79004",
				"desc" : "Referral code not found",
				"timestamp" : timestamp
			}
	except Exception as e:
		print("[Error] Failed to connect to redis : {}".format(e));
		return {
			"code" : "79005",
			"desc" : "Failed to connect to redis",
			"timestamp" : timestamp
		}
	
	return {
		"code" : "0",
		"desc" : "success",
		"timestamp" : timestamp,
		"data" : {
			"referral_code" : referralCode
		}
	}
