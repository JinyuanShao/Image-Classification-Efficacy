import numpy as np
from sklearn.metrics import confusion_matrix

class Efficacy():
    
    def __init__(self, ref_list, pred_list, label_values):
        '''
        Input reference data/ground truth, prediction, and label values
        previous two are 1-dim numpy array, and label values is a list
        '''
        self.ref_list = ref_list
        self.pred_list = pred_list
        self.label_values = label_values
        
        self.confusion_matrix = confusion_matrix(self.ref_list, self.pred_list, labels=self.label_values)
        self.num_classes = len(self.label_values)
    
    def MICE(self):
        '''
        Calculate MICE
        Return a percentile of mice, which means the performance of the classifier
        '''
    
        OA = np.trace(self.confusion_matrix)/np.sum(self.confusion_matrix)

        prop = (np.sum(self.confusion_matrix,axis=1))/(np.sum(self.confusion_matrix))

        prop_square = np.square(prop)
    
        prop_square_sum = np.sum(prop_square)
    
        mice = (OA-prop_square_sum)/(1-prop_square_sum)
    
        return mice
    
    def OICE(self):
        '''
        Calculate OICE
        Return a list of OICE of each class
        '''
        
        oice = []
    
        for i in range(self.num_classes):
            
            producer_accuracy = self.confusion_matrix[i][i]/np.sum(self.confusion_matrix[:,i])
            
            prop = (np.sum(self.confusion_matrix,axis=1))/(np.sum(self.confusion_matrix))
            
            prop_i = prop[i]
            
            OICE = (producer_accuracy - prop_i) / (1 - prop_i)
            
            oice.append(OICE)
            
        return oice
    
    def CICE(self):
        '''
        Calculate OICE
        Return a list of OCCE of each class
        '''
        
        cice = []
        
        for i in range(self.num_classes):
            
            user_accuracy = self.confusion_matrix[i][i]/np.sum(self.confusion_matrix[i,:])
            
            prop = (np.sum(self.confusion_matrix,axis=1))/(np.sum(self.confusion_matrix))
            
            prop_i = prop[i]
            
            CICE = (user_accuracy - prop_i) / (1 - prop_i)
            
            cice.append(CICE)

        return cice
