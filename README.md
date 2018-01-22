# Twitter Sink

Repository contains a driver to sink twitter statuses data to mongoDB and APIs to retrieve them.


### Prerequisites

- MongoDB
- Flask

### Installing

To create virtual environment and starting development server 

```
sh create_env.sh
```

Run application

```
export ENV=development
python manage.py runserver
```

command to sink status from twitter

```
python sink_to_mongo.py "keyword"
```

### Searching

URL - /status

```
/status?screen_name=JohnMiller
```

params

- screen_name
- retweet_count
- favorite_count
- created_at
- tweet_text
- language
- followers_count

params - created_at, retweet_count and favorite_count support range query
To use range query feature, append [_gt or _lt] to query_params

```
/status?screen_name=JohnMiller&retweet_count_gt=5
```

## TODO
- Add more filters

## Authors

* **Neeraj Gahlot** - *Initial work* - [Cerebro](https://github.com/Cerebro92)
