![alt text](https://github.com/ids-cv/Multi-Lingual-Visual-Grounding/blob/master/images/examples.png)

# Multi-Lingual-Visual-Grounding

Visual grounding, as an extension to object detection, is the task to locate objects in an image based on queries in natural language. It is a fundamental task in various multi-modal learning tasks. This project provides a benchmark for visual grounding tasks in French language. For more details, please refer to [our paper](https://ieeexplore.ieee.org/document/9305199).

## Dataset

We publish our crowdsourced dataset Flickr-30k French in this repository.

All 31k sentences (29k training sentences, 1k validation sentences, 1k test sentences) are annotated. In our paper, only the first 5k training sentences among 29k are used to demonstrate our transfer learning innovations. 

The French dataset that we annotated is in the folder French-data. 


## Model

We apply and adapt the DDPN model to first train the model on English dataset. Then innovative transfer learning techniques are used to train another model on French dataset, reaching similar performance with smaller training set (we show that only 5k French image-query pairs are enough).

Model overview: 

![alt text](https://github.com/ids-cv/Multi-Lingual-Visual-Grounding/blob/master/images/model.png)

If you use the dataset or the model in this repository, please cite our paper: 

    @ARTICLE{9305199,  author={W. {Dong} and M. {Otani} and N. {Garcia} and Y. {Nakashima} and C. {Chu}},
    journal={IEEE Access},   
    title={Cross-Lingual Visual Grounding},   
    year={2021},  volume={9},  number={},  pages={349-358},  
    doi={10.1109/ACCESS.2020.3046719}}
