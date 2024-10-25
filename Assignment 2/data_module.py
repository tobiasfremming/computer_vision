from torch.utils.data import DataLoader
from torchvision import datasets
import lightning as L


# DataModule to handle the MNIST dataset
class MNISTDataModule(L.LightningDataModule):
    def __init__(self, batch_size=64, transforms=None):
        super().__init__()
        self.batch_size = batch_size
        self.transform = transforms

    def prepare_data(self):
        datasets.MNIST(root='data', train=True, download=True)
        datasets.MNIST(root='data', train=False, download=True)

    def setup(self, stage=None):
        self.mnist_train = datasets.MNIST(root='data', train=True, transform=self.transform)
        self.mnist_test = datasets.MNIST(root='data', train=False, transform=self.transform)

    def train_dataloader(self):
        return DataLoader(self.mnist_train, batch_size=self.batch_size, shuffle=True, drop_last=True)

    def val_dataloader(self):
        return DataLoader(self.mnist_test, batch_size=self.batch_size, drop_last=True)