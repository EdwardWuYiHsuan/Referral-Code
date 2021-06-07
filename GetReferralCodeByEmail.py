import datetime
import redis

endpoint = "elasticache-savedeviceidandreferralcode.akto78.ng.0001.apne1.cache.amazonaws.com";

def lambda_handler(event, context):

	print("[Info] Request : {}".format(event));
	timestamp = datetime.datetime.utcnow().isoformat() + 'Z';

	email = event.get("email");
	if email is None:
		return {
			"code" : "0001",
			"desc" : "Invalid 'email'",
			"timestamp" : timestamp
		}

	try:
		redisClient = redis.StrictRedis(host=endpoint, port=6379, db=0, socket_timeout=1);
		referralCode = redisClient.get(email);
		if referralCode is None:
			return {
				"code" : "0004",
				"desc" : "Referral code not found",
				"timestamp" : timestamp
			}
	except:
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
			"referral_code" : referralCode
		}
	}
