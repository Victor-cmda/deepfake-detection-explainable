import torch

def check_gpu():
    """Verifica disponibilidade de GPU e exibe informações."""
    if torch.cuda.is_available():
        device_count = torch.cuda.device_count()
        print(f"GPU disponível! Encontradas {device_count} GPU(s).")
        for i in range(device_count):
            print(f"  GPU {i}: {torch.cuda.get_device_name(i)}")
        print(f"CUDA Version: {torch.version.cuda}")
    else:
        print("GPU não disponível. O modelo será executado na CPU.")
    
    return torch.cuda.is_available()

if __name__ == "__main__":
    check_gpu()
