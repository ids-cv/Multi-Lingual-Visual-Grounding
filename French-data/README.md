## This directory contains the 7k French visual grounding data crowdsourced on Amazon MTurk.

We follow the same data split as in Flickr30k Entities.

Flickr30k Entities has 5 sentences for each image, while we only have one. The sentence appearing in our dataset is the same sentence as in Multi30k's French dataset. 

The numbers of sentences in each set are:
  * training set: 5000 (the first 5000 images in the training set of Flickr30k Entities)
  * validation set: 1014 
  * test set: 1000

The files of split we use is downloaded from:

https://github.com/multi30k/dataset/tree/master/data/task1  (you can also find other useful data in Multi30k)

The three files involved in our dataset are also uploaded in the folder "split". 

The bounding box data can be found at the original Flickr30k Entities github page:

https://github.com/BryanPlummer/flickr30k_entities  (in the file annotations.zip)

## The format of the data

Example:

train\*\*0\*\*e\*\* [/EN#1/people deux jeunes hommes blancs] sont dehors près [/EN#4/scene de buissons] .

This is the first line in the training set. As you can see, the two consecutive stars are the seperator. 
  * The first mark, a value among 'train'/'val'/'test', indicates the set to which this line belongs.  
  * The second mark, a integer value, is the line position.
  * The third mark, always 'e', you can ignore this. 
  * Finally, the noted French sentence. 
