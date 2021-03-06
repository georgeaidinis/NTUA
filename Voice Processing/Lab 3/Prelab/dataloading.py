from torch.utils.data import Dataset
from tqdm import tqdm
import numpy
from nltk.tokenize import TweetTokenizer


class SentenceDataset(Dataset):
    """
    Our custom PyTorch Dataset, for preparing strings of text (sentences)
    What we have to do is to implement the 2 abstract methods:

        - __len__(self): in order to let the DataLoader know the size
            of our dataset and to perform batching, shuffling and so on...

        - __getitem__(self, index): we have to return the properly
            processed data-item from our dataset with a given index
    """

    def __init__(self, X, y, word2idx):
        """
        In the initialization of the dataset we will have to assign the
        input values to the corresponding class attributes
        and preprocess the text samples

        -Store all meaningful arguments to the constructor here for debugging
         and for usage in other methods
        -Do most of the heavy-lifting like preprocessing the dataset here


        Args:
            X (list): List of training samples
            y (list): List of training labels
            word2idx (dict): a dictionary which maps words to indexes
        """

        # self.data = X
        # self.labels = y
        # self.word2idx = word2idx

        # EX2
        #Twitter-aware tokenizer, designed to be flexible and easy to adapt to new domains and tasks.
 

        #Remove Twitter username handles from text.
        #Replace repeated character sequences of length 3 or greater with sequences of length 3.
        tokenizer = TweetTokenizer(strip_handles=True, reduce_len=True)

        for i in range(len(X)):
        	X[i] = tokenizer.tokenize(X[i])


        lengths = [len(x) for x in X]
        max_l = max(lengths)
        self.data = X
        self.labels = y
        self.word2idx = word2idx
        self.max_length = max_l



    def __len__(self):
        """
        Must return the length of the dataset, so the dataloader can know
        how to split it into batches

        Returns:
            (int): the length of the dataset
        """

        return len(self.data)

    def __getitem__(self, index):
        """
        Returns the _transformed_ item from the dataset

        Args:
            index (int):

        Returns:
            (tuple):
                * example (ndarray): vector representation of a training example
                * label (int): the class label
                * length (int): the length (tokens) of the sentence

        Examples:
            For an `index` where:
            ::
                self.data[index] = ['this', 'is', 'really', 'simple']
                self.target[index] = "neutral"

            the function will have to return something like:
            ::
                example = [  533  3908  1387   649   0     0     0     0]
                label = 1
                length = 4
        """

        # EX3

        # return example, label, length
        
        example = [0]*len(self.data[index])
        label  = self.labels[index]
        length = len(self.data[index])
        for i in range(len(example)):
            if self.data[index][i] in self.word2idx:
            	example[i] = self.word2idx[self.data[index][i]]
            else:
            	example[i] = self.word2idx['<unk>']
        diff = len(self.data[index]) - self.max_length
        if (diff<0):
            example += [0 for j in range(abs(diff))]
        return (numpy.array(example), label ,length)

