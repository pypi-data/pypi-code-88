import torch
import torchvision
import torch.nn as nn
import numpy as np
import torch.nn.functional as F
from torch.utils.data import DataLoader
from .visualize import plot_learning_rate,plot_metric,plot_result



def accuracy(outputs, labels):
              
    _, preds = torch.max(outputs, dim=1)
    return torch.tensor(torch.sum(preds == labels).item() / len(preds))



class trainer(nn.Module):


  def train_one_batch(self,batch,loss_func=F.cross_entropy):
    images,labels=batch
    
    return loss_func(self(images),labels)

  def validate_one_batch(self,batch,loss_func=F.cross_entropy,metric='accuracy'):
    images,labels=batch
    output_=self(images)
    loss=loss_func(output_,labels)
    if metric=='accuracy':
      met=accuracy(output_.detach(),labels)

    return {
        metric:met,
        "Loss":loss.detach()
    }

  def combining_data(self,data,metric='accuracy'):
    met=[dict_[metric] for dict_ in data]
    loss=[dict_['Loss'] for dict_ in data]

    return {
        "Val_loss":torch.stack(loss).mean().item(),
        "Val_"+metric:torch.stack(met).mean().item()
          }

  def epoch_end(self,final_result,epoch_number,metric='accuracy'):
      print("Epoch Number: ",epoch_number,end=' ')
      print("Training loss: ",final_result['Train_loss'],end=' ')
      print("Validation loss: ",final_result['Val_loss'],end=' ')
      print("Validation "+metric+" ",final_result['Val_'+metric])


  @torch.no_grad()
  def evaluate(self,val_loader,metric='accuracy'):
      self.eval()
      outputs = [self.validate_one_batch(batch,metric=metric) for batch in val_loader]

      return self.combining_data(outputs,metric)

  def get_lr(self,optimizer):
      for param_group in optimizer.param_groups:
          return param_group['lr']

  def fit(self,epochs, max_lr, train_loader, val_loader, 
                    weight_decay=0, grad_clip=None, opt_func=torch.optim.Adam,metric='accuracy',schedule_per_cycle=None):

      history = []
      
      optimizer = opt_func(self.parameters(), max_lr, weight_decay=weight_decay)
  
      if schedule_per_cycle is not None:
        sched = torch.optim.lr_scheduler.OneCycleLR(optimizer, max_lr, epochs=epochs, 
                                                  steps_per_epoch=len(train_loader))
      torch.cuda.empty_cache()
      for epoch in range(epochs):
          
          self.train()
          train_losses = []
          lrs = []
          for batch in train_loader:
              loss =self.train_one_batch(batch)
              train_losses.append(loss)
              loss.backward()
              
              if grad_clip: 
                  nn.utils.clip_grad_value_(self.parameters(), grad_clip)
              
              optimizer.step()
              optimizer.zero_grad()
              
              if schedule_per_cycle is not None:
                lrs.append(self.get_lr(optimizer))
                sched.step()
          
  
          result = self.evaluate(val_loader,metric)
          if schedule_per_cycle is not None:
            result['lrs'] = lrs
          result['Train_loss'] = torch.stack(train_losses).mean().item()
          self.epoch_end(result,epoch_number=epoch)
          history.append(result)

         
      plot_result(history)
      plot_metric(history,metric=metric)
      
      if schedule_per_cycle is not None:
         plot_learning_rate(history)
            
      return history

    

