import torch

from torch import nn


class BaselineDNN(nn.Module):
    """
    1. We embed the words in the input texts using an embedding layer
    2. We compute the min, mean, max of the word embeddings in each sample
       and use it as the feature representation of the sequence.
    4. We project with a linear layer the representation
       to the number of classes.ngth)
    """

    def __init__(self, output_size, embeddings, trainable_emb=False):
        """

        Args:
            output_size(int): the number of classes
            embeddings(bool):  the 2D matrix with the pretrained embeddings
            trainable_emb(bool): train (finetune) or freeze the weights
                the embedding layer
        """


#############################################################################
# Question 4
#############################################################################
# Creating the Embedding Layer

        super(BaselineDNN, self).__init__()
        #from the embeddings array given to us by the load_word_vectors function
        num_embeddings, emb_dim = embeddings.shape 
        # 1 - define the embedding layer
        self.embedding = nn.Embedding(num_embeddings=num_embeddings, embedding_dim=emb_dim)  # EX4

        # 2 - initialize the weights of our Embedding layer
        # from the pretrained word embeddings

        #This is done in the line just below, it's the arg torch.from_numpy(embeddings).

        #self.embedding.weight.data.copy_(torch.from_numpy(embeddings))  # EX4

        # 3 - define if the embedding layer will be frozen or finetuned
        self.embedding.weight = nn.Parameter(torch.from_numpy(embeddings), requires_grad=trainable_emb)  # EX4

        # 4 - define a non-linear transformation of the representations
        self.non_linear_transformation1 = nn.ReLU()  # EX5
        self.non_linear_transformation2 = nn.Tanh()

        # 5 - define the final Linear layer which maps
        # the representations to the classes
        self.classifier = nn.Linear(in_features=emb_dim, out_features=output_size)  # EX5

    def forward(self, x, lengths):
        """
        This is the heart of the model.
        This function, defines how the data passes through the network.

        Returns: the logits for each class

        """

        # 1 - embed the words, using the embedding layer
        embeddings = self.embedding(x)  # EX6

        # 2 - construct a sentence representation out of the word embeddings

        #We are going to create a simple represantation, using the average
        #(center of mass) of the word embeddings in a sentence


        dimension_sums = torch.sum(embeddings, dim = 1)            #sum over columns   
        l = lengths.view(-1, 1).expand(dimension_sums.size(0), dimension_sums.size(1))
        representation =  dimension_sums / l.float() # EX6

        

        # 3 - transform the representations to new ones.


        representations = self.non_linear_transformation1(representation)  # EX6

        # 4 - project the representations to classes using a linear layer
        logits = self.classifier(representation)  # EX6

        return logits
