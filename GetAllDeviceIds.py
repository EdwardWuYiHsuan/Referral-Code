import datetime
import redis


endpoint = "elasticache-savedeviceidandreferralcode.akto78.ng.0001.apne1.cache.amazonaws.com";

def lambda_handler(event, context):

	timestamp = datetime.datetime.utcnow().isoformat() + 'Z';
	
	try:
		redisClient = redis.StrictRedis(host=endpoint, port=6379, db=0, socket_timeout=1);
		deviceIds = redisClient.keys();  #keys = <class 'list'>
		
		#redisClient.flushdb();  # Delete all keys in the current database.
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
			"device_ids" : deviceIds
		}
	}
