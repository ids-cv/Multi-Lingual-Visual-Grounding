## This directory contains the 31k French visual grounding data crowdsourced on Amazon MTurk.

We follow the same data split as in Flickr30k Entities.

There is one sentence for each image. The sentence appearing in our dataset is the same sentence as in Multi30k's French dataset. 

The numbers of sentences in each set are:
  * training set: 29000
  * validation set: 1014 
  * test set: 1000

The files of split we use is downloaded from:

https://github.com/multi30k/dataset/tree/master/data/task1  (you can also find other useful data in Multi30k)

The three files involved in our dataset are also uploaded in the folder "split". 

The bounding box data can be found at the original Flickr30k Entities github page:

https://github.com/BryanPlummer/flickr30k_entities  (in the file annotations.zip)

## The format of the data

Example:

train\*\*0\*\* [/EN#1/people deux jeunes hommes blancs] sont dehors près [/EN#4/scene de buissons] .

This is the first line in the training set. As you can see, the two consecutive stars are the seperator. 
  * The first part, a value among 'train'/'val'/'test', indicates the set to which this line belongs.  
  * The second part, an integer value, is the line position.
  * Finally, the noted French sentence. 
