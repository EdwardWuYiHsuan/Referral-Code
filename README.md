# Referral-Code
Backend API for referral code

<!-- API -->
## Push email and referral code
`POST {server-url}/push_email_and_referral_code`

> Request

```json
{
    "email" : "String",
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
| email                  | STRING |        |       |             |
| referral_code          | STRING |        |       |             |


### Return Error
- 10001 Invalid 'email'
- 10002 Invalid 'referral_code'
- 10003 Failed to push data
- 10004 Referral code not found
- 10005 Failed to connect to redis


<!-- API -->
## Get referral code by email

`GET {server-url}/get_referral_code_by_email/{email}`

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
| email                  | STRING |        |       |             |

### Parameters
None

### Return Error
- 10001 Invalid 'email'
- 10002 Invalid 'referral_code'
- 10003 Failed to push data
- 10004 Referral code not found
- 10005 Failed to connect to redis

<!-- API -->
## Get all emails

`GET {server-url}/get_all_emails`

> Request

```json
```

> Response

```json
{
    "code": "0",
    "desc": "success",
    "timestamp": "2021-06-07T18:39:57.214487Z",
    "data": {
        "emails": [
            "Ole5@gmail.com",
            "Lurline36@yahoo.com",
            "Jerrold13@gmail.com"
        ]
    }
}
```

### Header
| Key          | Value            |
| ------------ | ---------------- |
| Content-Type | application/json |

### URL Parameters
None

### Parameters
None

### Return Error
- 10001 Invalid 'email'
- 10002 Invalid 'referral_code'
- 10003 Failed to push data
- 10004 Referral code not found
- 10005 Failed to connect to redis

