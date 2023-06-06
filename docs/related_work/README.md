# PrimateFace: Bridging the gap in primate face analysis

PrimateFace is notable as the first large-scale cross-primate species face dataset.

Here's a non-inclusive snapshot of related work:


| Task                          | Source            | Species or Family             | Dataset          | Image Count | Model available? |
|-------------------------------|-------------------|-------------------------------|------------------|-------------|------------------|
| Face Detection                | Yang et al., 2016 | Human                         | WIDERFace        | 32,203      | Yes (mmdetection)|
| Face Detection + Identity     | Loos & Ernst 2013 | Chimp                         | Data for purchase | 6,522       | No               |
| Face Detection + Identity     | Guo et al., 2020  | 17 primate, 4 carnivore species | Animal Face Data (AFD) | 1,032 | No           |
| Face Detection + Keypoints (68)| Sagonas et al., 2013 | Human                       | 300-W            | 600         | Yes (mmpose)     |
| Face Detection + Keypoints (55)| Witham et al., 2018 | Macaque                     | Macaque Faces    | 4,000       | Yes (DeepLabCut) |
| Face Detection + Keypoints (68)| Jin et al., 2020  | Human                        | COCO (WholeBody) | 200,000     | Yes (mmpose)     |
| Face Detection + Keypoints (9) | Khan et al., 2020 | 334 species                  | AnimalWeb        | 21,921      | No               |
| Face Keypoints (5)            | Freytag et al., 2016 | Chimp                       | C-Zoo + C-Tai    | 6,486       | No               |
| Face Detection + Keypoints (68)   | Ours              | All primates                 | PrimateFace      | 300,000     | Yes (mmdetection, mmpose) |

On the other hand, there has been a TON of work towards quantifying natural primate behavior. Here are some relevant datasets and models addressing this goal:

| Task                        | Source          | Species or Family | Dataset               | Image Count            | Model available?   |
|-----------------------------|-----------------|-------------------|-----------------------|------------------------|--------------------|
| Animal Pose Estimation      | Yu et al., 2021 | Cross-species     | AP10k                 | 10,015 (675 primates)  | Yes (mmpose)       |
| NHP Body Pose Estimation    | Bala et al., 2020| Macaque           | OpenMonkeyStudio      | 195,228                | Yes                |
| NHP Body Pose Estimation    | Labuguen et al., 2021 | Macaque       | Not available         | Not available          | Yes (DeepLabCut)  |
| NHP Body Pose Estimation    | Yao et al., 2022 | Monkey            | OpenMonkeyChallenge   | 111,529                | No                 |
| NHP Body Pose Estimation    | Desai et al., 2022 | Apes            | OpenApePose           | 71,868                 | Yes                |
| Body Pose + Identity + Behavior | Marks et al., 2022 | Primate, mouse | Available upon request | Available upon request | Yes            |
| Face Detection + Keypoints (68)  | Ours            | All primates      | PrimateFace           | 300k                   | Yes (mmdetection, mmpose) |


# References
[1]	Maestripieri, Dario, and Christy L. Hoffman. "Behavior and social dynamics of rhesus macaques on Cayo Santiago." Bones, genetics, and behavior of rhesus macaques: Macaca mulatta of Cayo Santiago and beyond. New York, NY: Springer New York, 2011. 247-262.
[2]	Waller, Bridget M., and Jérôme Micheletta. "Facial expression in nonhuman animals." Emotion Review 5.1 (2013): 54-59.
[3]	Knaebe, Brenna, et al. "The promise of behavioral tracking systems for advancing primate animal welfare." Animals 12.13 (2022): 1648.
[4]	Ekman, Paul, and Wallace V. Friesen. "Facial action coding system." Environmental Psychology & Nonverbal Behavior (1978).
[5]	Parr, Lisa A., et al. "Brief communication: MaqFACS: a muscle‐based facial movement coding system for the rhesus macaque." American journal of physical anthropology 143.4 (2010): 625-630.
[6]	Vick, Sarah-Jane, et al. "A cross-species comparison of facial morphology and movement in humans and chimpanzees using the facial action coding system (FACS)." Journal of nonverbal behavior 31 (2007): 1-20.
[7]	Correia-Caeiro, Catia, et al. "Callifacs: The common marmoset facial action coding system." PloS one 17.5 (2022): e0266442.
[8]	Scheider, Linda, et al. "Social use of facial expressions in hylobatids." PloS one 11.3 (2016): e0151733.
[9]	Caeiro, Cátia C., et al. "OrangFACS: A muscle-based facial movement coding system for orangutans (Pongo spp.)." International Journal of Primatology 34 (2013): 115-129.
[10]	Kumar, Ashu, Amandeep Kaur, and Munish Kumar. "Face detection techniques: a review." Artificial Intelligence Review 52 (2019): 927-948.
[11]	Bettadapura, Vinay. "Face expression recognition and analysis: the state of the art." arXiv preprint arXiv:1203.6722 (2012).
[12]	Yang, Shuo, et al. "Wider face: A face detection benchmark." Proceedings of the IEEE conference on computer vision and pattern recognition. 2016.
[13]	Lin, Tsung-Yi, et al. "Microsoft coco: Common objects in context." Computer Vision–ECCV 2014: 13th European Conference, Zurich, Switzerland, September 6-12, 2014, Proceedings, Part V 13. Springer International Publishing, 2014.
[14]	Jin, Sheng, et al. "Whole-body human pose estimation in the wild." Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part IX 16. Springer International Publishing, 2020.
[15]	Sagonas, Christos, et al. "300 faces in-the-wild challenge: The first facial landmark localization challenge." Proceedings of the IEEE international conference on computer vision workshops. 2013.
[16]	Koestinger, Martin, et al. "Annotated facial landmarks in the wild: A large-scale, real-world database for facial landmark localization." 2011 IEEE international conference on computer vision workshops (ICCV workshops). IEEE, 2011.¬
[17]	Loos, Alexander, and Andreas Ernst. "An automated chimpanzee identification system using face detection and recognition." EURASIP Journal on Image and Video Processing 2013 (2013): 1-17.
[18]	Freytag, Alexander, et al. "Chimpanzee faces in the wild: Log-euclidean CNNs for predicting identities and attributes of primates." Pattern Recognition: 38th German Conference, GCPR 2016, Hannover, Germany, September 12-15, 2016, Proceedings 38. Springer International Publishing, 2016.
[19]	Deb, Debayan, et al. "Face recognition: Primates in the wild." 2018 IEEE 9th International Conference on Biometrics Theory, Applications and Systems (BTAS). IEEE, 2018.
[20]	Witham, Claire L. "Automated face recognition of rhesus macaques." Journal of neuroscience methods 300 (2018): 157-165.
[21]	Crunchant, Anne‐Sophie, et al. "Automated face detection for occurrence and occupancy estimation in chimpanzees." American journal of primatology 79.3 (2017): e22627.
[22]	Blumrosen, Gaddi, David Hawellek, and Bijan Pesaran. "Towards automated recognition of facial expressions in animal models." Proceedings of the IEEE International Conference on Computer Vision Workshops. 2017.
[23]	Guo, Songtao, et al. "Automatic identification of individual primates with deep learning techniques." Iscience 23.8 (2020): 101412.
[24]	Khan, Muhammad Haris, et al. "Animalweb: A large-scale hierarchical dataset of annotated animal faces." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020.
[25]	Yu, Hang, et al. "Ap-10k: A benchmark for animal pose estimation in the wild." arXiv preprint arXiv:2108.12617 (2021).
[26]	Bala, Praneet C., et al. "Automated markerless pose estimation in freely moving macaques with OpenMonkeyStudio." Nature communications 11.1 (2020): 4560.
[27]	Labuguen, Rollyn, et al. "MacaquePose: a novel “in the wild” macaque monkey pose dataset for markerless motion capture." Frontiers in behavioral neuroscience 14 (2021): 581154.
[28]	Yao, Yuan, et al. "OpenMonkeyChallenge: Dataset and Benchmark Challenges for Pose Estimation of Non-human Primates." International Journal of Computer Vision 131.1 (2023): 243-258.
[29]	Desai, Nisarg, et al. "OpenApePose: a database of annotated ape photographs for pose estimation." arXiv preprint arXiv:2212.00741 (2022).
[30]	Marks, Markus, et al. "Deep-learning-based identification, tracking, pose estimation and behaviour classification of interacting primates and mice in complex environments." Nature machine intelligence 4.4 (2022): 331-340.¬
[31]	Rasmus, Antti, et al. "Semi-supervised learning with ladder networks." Advances in neural information processing systems 28 (2015).
[32]	Rawlins, Richard G., and Matt J. Kessler, eds. The Cayo Santiago macaques: History, behavior, and biology. SUnY Press, 1986.
[33]	Dwyer, B., Nelson, J. (2022), Solawetz, J., et. al. Roboflow (Version 1.0) [Software]. Available from https://roboflow.com. computer vision.
[34]	Liu, Wei, et al. "Ssd: Single shot multibox detector." Computer Vision–ECCV 2016: 14th European Conference, Amsterdam, The Netherlands, October 11–14, 2016, Proceedings, Part I 14. Springer International Publishing, 2016.
[35]	Cleanlab (2023). Cleanvision (Version 0.2.1) [Software], Available from https://github.com/cleanlab/cleanvision.
[36]	Radford, Alec, et al. "Learning transferable visual models from natural language supervision." International conference on machine learning. PMLR, 2021.
[37]	Zhang, Hao, et al. "Dino: Detr with improved denoising anchor boxes for end-to-end object detection." arXiv preprint arXiv:2203.03605 (2022).
[38]	Xu, Yufei, et al. "Vitpose: Simple vision transformer baselines for human pose estimation." arXiv preprint arXiv:2204.12484 (2022).
[39]	Mathis, Alexander, et al. "DeepLabCut: markerless pose estimation of user-defined body parts with deep learning." Nature neuroscience 21.9 (2018): 1281-1289.
[40]	Ye, Shaokai, Alexander Mathis, and Mackenzie Weygandt Mathis. "Panoptic animal pose estimators are zero-shot performers." arXiv preprint arXiv:2203.07436 (2022).

