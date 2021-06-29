import datetime
#import redis
from rediscluster import RedisCluster


redisPassword = "stupidpass"
redisClusterNodes = [{"host": "127.0.0.1", "port": "7001"}, {"host": "127.0.0.1", "port": "7002"}, 
					 {"host": "127.0.0.1", "port": "7003"}, {"host": "127.0.0.1", "port": "7004"}, 
					 {"host": "127.0.0.1", "port": "7005"}, {"host": "127.0.0.1", "port": "7006"}]


# def lambda_handler(event, context):
def lambda_handler():

	timestamp = datetime.datetime.utcnow().isoformat() + 'Z';
	
	try:

		#redisClient = redis.StrictRedis(host=endpoint, port=6379, db=0, socket_timeout=1);
		# redisClient.flushdb();  # Delete all keys in the current database.


		redisCluster = RedisCluster(startup_nodes=redisClusterNodes, decode_responses=True, skip_full_coverage_check=True, password=redisPassword)

		keys = redisCluster.keys();
		print("[Edward's test] keys : {}".format(keys));
		print("[Edward's test] keys : {}".format(type(keys)));  # keys = <class 'list'>

		setResult = redisCluster.set("music", "classic");
		print("[Edward's test] setResult : {}".format(setResult));
		print("[Edward's test] setResult : {}".format(type(setResult)));  # setResult = <class 'bool'>, type is boolean

		value = redisCluster.get("music");
		print("[Edward's test] value : {}".format(value));
		print("[Edward's test] value : {}".format(type(value)));  # value = <class 'str'>, type is string
		
	except Exception as e: 
		print("[Error] Failed to connect to redis : {}".format(e));


lambda_handler();