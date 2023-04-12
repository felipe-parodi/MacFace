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


