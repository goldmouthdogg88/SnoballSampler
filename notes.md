# Overview


I want to create an app that does the following:

1. start with a seed query such as "Python Inheritance"
2. From that seed get a list of output URLS
3. From that url build a structure of information...consider the following



### Example (Instance)

```JSON
{
	"seed_query": "how to spider the dark web",
	"seed_query_SERP_data": [
		"https://www.theatlantic.com/technology/archive/2016/02/the-spider-that-crawls-the-dark-web-looking-for-stolen-data/470220/",
		"https://luxuryslife.fandom.com/wiki/Black_Goliath_Spider.",
		"https://ache.readthedocs.io/en/latest/tutorial-crawling-tor.html"
	],
	"visited_SERP_urls": [{
		"webpage_title": "How To Scrape the Dark Web",
		"url": "https://towardsdatascience.com/how-to-scrape-the-dark-web-53145add7033",
		"data": {
			"raw_data": "/path/to/raw/data.*",
      "id": "001",
      "user_defined_terms": [
        
      ],
      "user_defined_phrases": [
        "scrape the website in chunks"
      ]
      "sub_links": [
        "https://towardsdatascience.com/how-to-locate-dark-web-hacker-forums-for-security-research-e87b53f18508",
        
      ]
      "tokens": "",
			"processed_data": {
			  	"tokens": "",
				"global_unique_tokens": "Tokens that are unique to this raw file",
				"queue_unique_tokens": "Number of unique tokens compaired against n files",
				"matching_tokens": "",
				"collocations": "",
        "extracted_terms": []
        
			},
		},
		"session": {
			"topic": "",
			"visitedAt": "",
			"branching_query_terms": [],
      "session_id": "",
      "session_name": "",
      "machine_origin": "",
      "browser": "",
      "createdAt": ""
		}
	}]
}
```