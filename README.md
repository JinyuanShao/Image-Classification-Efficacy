# Image Classification Efficacy (ICE): A better metric for evaluating the discriminative power of a classifier


Image Classification Efficacy (ICE) is introduced for comparing classification methods that are tested with different datasets. It can be used in various fields to consistently evaluate the performance of any classifiers.

This is general Python code of ICE implementation. For the principles of ICE metrics, please refer to original paper: https://ieeexplore.ieee.org/abstract/document/9551959

- **MICE**:  **M**ap-level **I**mage **C**lassification **E**fficacy

![](https://latex.codecogs.com/svg.image?\mathrm{MICE}=\frac{OA-\sum_{j=1}^{n}\left(\frac{n_{&plus;j}}{n}\right)^{2}}{1-\sum_{j=1}^{n}\left(\frac{n_{&plus;j}}{n}\right)^{2}})

- **CICE**: **C**ommission-error-based **I**mage **C**lassification **E**fficacy

![](https://latex.codecogs.com/svg.image?\mathrm{CICE}_{j}=\frac{{UA}_{j}-\frac{n_{&plus;j}}{n}}{1-\frac{n_{&plus;j}}{n}})

- **OICE**: **O**mission-error-based **I**mage **C**lassification **E**fficacy

![](https://latex.codecogs.com/svg.image?\mathrm{OICE}_{j}=\frac{{PA}_{j}-\frac{n_{&plus;j}}{n}}{1-\frac{n_{&plus;j}}{n}})

Where, njj is the number or percent of sample points classified as class j, n+j is the class total from reference data, nj+ is the class total from classification result (predicted data), J is the total number of classes, and n is the total number of samples.

## Usage



The computation of **ICE** metrics expects reference data and predicted data in Numpy list format with one dimension, and also a Python list that contains the value of labels.



```python
from assessment import Efficacy

efficacy = Efficay(ref_list=gt_list_arr, pred_list=pred_list_arr, label_values=[0,1]) # binary classificaion

mice = efficacy.MICE()
oice = efficacy.OICE()
cice = efficacy.CICE()
```



## Citing

If our ICE metrics are helpful to your research or projects, please consider to cite our paper:
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
