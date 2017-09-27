This is an effort to transcribe all 3500+ pages of Jeph Jacques's Questionable Content. 

## Scrape
1. Grab all QC strips

## Read Speech Balloon Text
1. Segment image to isolate speech balloons
2. Clean up and feed into OCR pipeline
  * Figure out how to improve OCR quality
    * Higher-res images would help
  * Add QC lingo and character names to 
  
## Identify Characters
1. Segment image to isolate humanoid figures
2. Train neural net to label characters
  * Approx. 3k strips, say 5 character drawings per strip, around 30 characters

## Attribute Speech
1. Follow speech bubble to character's head. No clue. 

## Endpoint
What will this be? Web app that takes QC url or issue number and returns transcript? Massive dump, with daily updates, to fan wiki? TBD.
