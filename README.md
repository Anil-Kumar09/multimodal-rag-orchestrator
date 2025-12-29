# multimodal-rag-orchestrator

The project requires Pytorch 

- Install Pytorch if your system has a [CUDA enabled](https://developer.nvidia.com/cuda/gpus) Graphics card

```
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu128
```


- if no graphics card available, use below command : 

```
pip3 install torch torchvision
```

- check whether CUDA driver is enabled 

```
import torch 
torch.cuda.is_available()