import torch

embeddings = torch.rand(10, 300)
first_vector = embeddings[0]
print(first_vector.shape)  # torch.Size([300])
