import numpy as np
from sklearn.metrics import confusion_matrix

def MICE(ref_list, pred_list,label_values):
    
    cms = confusion_matrix(ref_list, pred_list, labels=label_values)
    
     
    OA = np.trace(cms)/np.sum(cms)
    
    
    prop = (np.sum(cms,axis=1))/(np.sum(cms))
    
    
    prop_square = np.square(prop)
    
    
    prop_square_sum = np.sum(prop_square)
    
    
    mice = (OA-prop_square_sum)/(1-prop_square_sum)
    
    
    return round(mice,2)