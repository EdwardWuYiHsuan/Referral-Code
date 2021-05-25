import datetime
import redis


endpoint = "elasticache-savedeviceidandreferralcode.akto78.ng.0001.apne1.cache.amazonaws.com";

def lambda_handler(event, context):
	
	print("[Info] Request : {}".format(event));
	timestamp = datetime.datetime.utcnow().isoformat() + 'Z';
	
	deviceId = event.get("device_id");
	if deviceId is None:
		return {
			"code": "0001",
			"desc" : "Invalid 'device_id'",
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
		redisClient = redis.StrictRedis(host=endpoint, port=6379, db=0, socket_timeout=1);
		result = redisClient.set(deviceId, referralCode);  # type is boolean
	except:
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
