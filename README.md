# MICE: Map-level Image Classification Efficacy



MICE is introduced for comparing classification methods that are tested with different datasets. It could be used in any visual tasks to evaluated the performance of the classifiers.



This is official implementation Python code of MICE. Original paper: https://ieeexplore.ieee.org/abstract/document/9551959



## Usage



**MICE** expects reference data and predicted data in Numpy list format with one dimension, and also a Python list that contains the value of labels.



```python
from efficacy import MICE

mice = MICE(ref_list=gt_list_arr, pred_list=pred_list_arr, label_values=[0,1]) # binary classification
```



## Citing

If our MICE is helpful to your research or projects, please consider to refer our paper:
```
@article{shao2021introducing,
  title={Introducing image classification efficacies},
  author={Shao, Guofan and Tang, Lina and Zhang, Hao},
  journal={IEEE Access},
  volume={9},
  pages={134809--134816},
  year={2021},
  publisher={IEEE}
}
```
