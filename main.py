from __future__ import print_function
import torch 

def main():
  
    x = torch.rand(5, 3)
    print(x)
    print(
torch.cuda.is_available())

    
main()