# Referral-Code
Backend API for referral code

<!-- API -->
## Push deviceId and referral code
`POST {server-url}/push_deviceid_and_referral_code`

> Request

```json
{
    "device_id" : "String",
    "referral_code" : "String"
}
```

> Response

```json
{
    "code": "0",
    "desc": "success",
    "timestamp": "2021-05-25T06:44:32.914614Z"
}
```

### Header
| Key          | Value            |
| ------------ | ---------------- |
| Content-Type | application/json |

### URL Parameters
None

### Parameters
| Parameter              | Type   | Length | Value | Description |
| ---------------------- | ------ | ------ | ----- | ----------- |
| device_id              | STRING |        |       |             |
| referral_code          | STRING |        |       |             |


### Return Error
- 10001 Invalid 'device_id'
- 10002 Invalid 'referral_code'
- 10003 Failed to push data
- 10004 Referral code not found
- 10005 Failed to connect to redis


<!-- API -->
## Get referral code by deviceId

`GET {server-url}/get_referral_code_by_deviceid/{device_id}`

> Request

```json
```

> Response

```json
{
    "code": "0",
    "desc": "success",
    "timestamp": "2021-05-25T06:45:00.724573Z",
    "data": {
        "referral_code": "turquoise-396"
    }
}
```

### Header
| Key          | Value            |
| ------------ | ---------------- |
| Content-Type | application/json |

### URL Parameters
| Parameter              | Type   | Length | Value | Description |
| ---------------------- | ------ | ------ | ----- | ----------- |
| device_id              | STRING |        |       |             |

### Parameters
None

### Return Error
- 10001 Invalid 'device_id'
- 10002 Invalid 'referral_code'
- 10003 Failed to push data
- 10004 Referral code not found
- 10005 Failed to connect to redis

