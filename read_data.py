import wfdb
import pandas as pd

def label_reader(type, sub, ses):
    '''
    Get the label for each task.

    Parameters: 
    - type: 'dynamic' or 'maintenance'
    - sub: number of subject(1 to 20)
    - ses: number of session(1 or 2)

    Returns:
    - label: n*1 pandas dataframe, n is the number of tasks
    '''
    label = pd.read_csv(f'./pr_dataset/subject0{sub}_session{ses}/label_{type}.txt', 
                        header=None)
    label = label.transpose()
    label.columns = ['label']
    return label

def data_reader(type, sub, ses, task):
    '''
    Get the data of specific task.
    '''
    filename = f'./pr_dataset/subject0{sub}_session{ses}/{type}_preprocess_sample{task}'
    record = wfdb.rdrecord(filename)
    df = record.to_dataframe()
    return df