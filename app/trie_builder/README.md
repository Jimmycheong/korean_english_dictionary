# korean_dictionary

The following project builds on my Trie Search Engine repository

# Setup

1. Clone the project using terminal into a suitable location 

2. Go into the project directory using the cd command

3. The final data dumped can be curled into a json file as such:
```
curl http://benhumphreys.ca/kdict/kdict_dump.json > resources/json/final_dump.json
```


4a. To obtain the term ranking data: 
```
curl http://polydog.org/index.php?attachments/%E1%84%83%E1%85%A9%E1%84%81%E1%85%A2%E1%84%87%E1%85%B5-dialogs-zip.251/ > term_ranking/goblin_transcripts.zip 

unzip goblin_transcripts.zip 

mv 도깨비 dialogs goblin_transcripts
```

4b. Then run the python script to create a dictionary of terms with frequency counts: 

```
python term_ranking_scraper.py goblin_transcripts
```
