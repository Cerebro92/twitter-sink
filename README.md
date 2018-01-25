# Twitter Sink

Repository contains a driver to sink twitter statuses data to mongoDB and APIs to retrieve them.

### Prerequisites

- MongoDB
- Flask

### Installing

To create virtual environment and starting development server 

```
$ sh create_env.sh
```

Run application

```
$ export ENV=development
$ python manage.py runserver
```
This will start a development server at port 9854. Before starting server, make sure that ENV variable is exported and corresponding environment class exists in `app/configuration.py` file. To use `DevelopmentConfig` configs, set ENV as development. similar logic for other configs. 

### APIs

* API to sync keyword in MongoDB - /api/tweets
* API to fetch tweets from DB - /api/tweet_filters

### Sink API
This API is used add/remove keywords [to sink] in DB. 

To add new keyword
```
curl -X POST 
  http://127.0.0.1:9854/api/tweet_filters 
  -d '{
	"q": "USA"
}'
```
To remove a keyword
```
curl -X DELETE 
  http://127.0.0.1:9854/api/tweet_filters 
  -d '{
	"q": "USA"
}'
```
To list current keyword
```
curl -X GET 
  http://127.0.0.1:9854/api/tweet_filters 
```

### Tweet Filter API

Currently we are syncing following fields. All of them are queryable. 
- tweet_text
- name
- screen_name
- retweet_count
- favorite_count
- followers_count
- created_at
- language
- geo_location

Range Query Supported Fields
- retweet_count
- favorite_count
- followers_count
- created_at

Above fields support exact as well as range
To use range query, append _gt or _lt after field name. See Examples.

Sub string Supported fields
- name
- tweet text

Geo Location supported fields
- geo_location

Currently, geo_location filter returns records with in 100 meters of center point.

Examples

```
GET /api/tweets?language=en
GET /api/tweets?created_at_gt=2018-01-25T03:11:06+00:00&language=en
GET /api/tweets?geo_location=-115.0172734,36.08620206
```

All above queries results can be downloaded in csv format
```
GET /api/tweets?language=en&format=csv
```

## TODO
- Add more filters
- Custom Range for geo coordinates
- Persist filter keywords

## Authors

* **Neeraj Gahlot** - *Initial work* - [Cerebro](https://github.com/Cerebro92)
