import torch.nn as nn
import torch.optim as optim
import lightning.pytorch as pl
from torchmetrics import Accuracy

# Define the fully connected neural network
class LightningModule(pl.LightningModule):
    def __init__(self, model, lr, optimizer ):
        super(LightningModule, self).__init__()
        
        self.model = model
        self.lr = lr
        self.optimizer = optimizer
        self.loss_fn = nn.CrossEntropyLoss()
        self.acc_fn = Accuracy(task="multiclass", num_classes=10)

    def forward(self, x):
        y_hat = self.model(x)
        return y_hat

    def training_step(self, batch, batch_idx):
        images, labels = batch
        outputs = self.forward(images)
        loss = self.loss_fn(outputs, labels)
        
        # Log training accuracy
        acc = self.acc_fn(outputs, labels)
        self.log_dict({'train_acc': acc,    # Log training accuracy
                       'train_loss': loss},  # Log training loss
                      on_step=True, on_epoch=False)
        
        return loss

    def validation_step(self, batch, batch_idx):
        images, labels = batch
        outputs = self.forward(images)
        loss = self.loss_fn(outputs, labels)
        
        # Log validation loss and accuracy
        acc = self.acc_fn(outputs, labels)
        self.log_dict({'val_acc': acc,    # Log training accuracy
                       'val_loss': loss},  # Log training loss
                      on_step=False, on_epoch=True, prog_bar=True)
        
        return loss

    def configure_optimizers(self):
        return self.optimizer(self.parameters(), lr=self.lr)


