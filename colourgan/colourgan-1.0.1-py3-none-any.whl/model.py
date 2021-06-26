'''Model Class for ColourGAN.'''
import os
import torch
import numpy as np
import cv2
import torch.nn.functional as F
from colourgan.networks import (
    Generator ,
    Discriminator
)
from colourgan.config import get_cfg
from colourgan.data import Cifar10Dataset
from colourgan.utils import save_losses
from colourgan.logger import logger

class ColourGAN:
    '''Wrapper Class for ColourGAN.'''
    def __init__(self,config,inference=False):
        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        self.cfg = config
        self.generator = Generator(self.cfg.generator_normalization)
        if not inference:
            self.discriminator = Discriminator(self.cfg.discriminator_normalization)
        if self.cfg.initial_weights_generator is not None:
            self.generator.load_state_dict(torch.load(self.cfg.initial_weights_generator,map_location = torch.device(device)))
            logger.info(f'Generator Weights Loaded from {self.cfg.initial_weights_generator}')
        if self.cfg.initial_weights_discriminator is not None:
            if not inference:
                self.discriminator.load_state_dict(torch.load(self.cfg.initial_weights_discriminator,map_location = torch.device(device)))
                logger.info(f'Discriminator Weights Loaded from {self.cfg.initial_weights_discriminator}')


    def train(self,train_loader,test_loader,epochs=20,pretrained=None):
        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        # Logging of device
        self.generator.to(device)
        self.discriminator.to(device)

        data_loaders = {
            'train': train_loader ,
            'test': test_loader
        }
        optimizers = {
            'gen': torch.optim.Adam(self.generator.parameters(),
                                    lr=self.cfg.base_lr_generator,
                                    betas=(0.5, 0.999)),
            'disc': torch.optim.Adam(self.discriminator.parameters(),
                                     lr=self.cfg.base_lr_discriminator,
                                     betas=(0.5, 0.999))
        }

        losses = {
            'l1': torch.nn.L1Loss(reduction='mean'),
            'disc': torch.nn.BCELoss(reduction='mean')
        }

        if not os.path.exists(self.cfg.output_path):
            os.makedirs(self.cfg.output_path)

        if pretrained is not None:
            # we need to load the weight dictionaries
            self.generator.load_state_dict(torch.load(
                pretrained['gen'],
                map_location=device
            ))
            self.discriminator.load_state_dict(torch.load(
                pretrained['disc'],
                map_location=device
            ))

        global_step = 0
        for epoch in range(epochs):
            print(f'Epoch: {epoch}')
            for phase in ['train', 'test']:

                # running losses for generator
                epoch_gen_adv_loss = 0.0
                epoch_gen_l1_loss = 0.0

                # running losses for discriminator
                epoch_disc_real_loss = 0.0
                epoch_disc_fake_loss = 0.0
                epoch_disc_real_acc = 0.0
                epoch_disc_fake_acc = 0.0

                if phase == 'train':
                    print('TRAINING:')
                else:
                    print('VALIDATION:')

                for idx, sample in enumerate(data_loaders[phase]):

                    # get data
                    img_l, real_img_lab = sample[:, 0:1, :, :].float().to(device), sample.float().to(device)

                    # generate targets
                    target_ones = torch.ones(real_img_lab.size(0), 1).to(device)
                    target_zeros = torch.zeros(real_img_lab.size(0), 1).to(device)

                    if phase == 'train':
                        # adjust LR
                        global_step += 1
                        self.__adjust_lr(optimizers['gen'], global_step, base_lr=self.cfg.base_lr_generator,
                                             lr_decay_rate=self.cfg.lr_decay, lr_decay_steps=self.cfg.lr_decay_steps)
                        self.__adjust_lr(optimizers['disc'], global_step, base_lr=self.cfg.base_lr_discriminator,
                                             lr_decay_rate=self.cfg.lr_decay, lr_decay_steps=self.cfg.lr_decay_steps)

                        # reset generator gradients
                        optimizers['gen'].zero_grad()

                    # train / inference the generator
                    with torch.set_grad_enabled(phase == 'train'):
                        fake_img_ab = self.generator(img_l)
                        fake_img_lab = torch.cat([img_l, fake_img_ab], dim=1).to(device)

                        #print(fake_img_lab.shape)
                        # adv loss
                        adv_loss = losses['disc'](self.discriminator(fake_img_lab), target_ones)
                        # l1 loss
                        l1_loss = losses['l1'](real_img_lab[:, 1:, :, :], fake_img_ab)
                        # full gen loss
                        full_gen_loss = (1.0 - self.cfg.l1_weight) * adv_loss + (self.cfg.l1_weight * l1_loss)

                        if phase == 'train':
                            full_gen_loss.backward()
                            optimizers['gen'].step()

                    epoch_gen_adv_loss += adv_loss.item()
                    epoch_gen_l1_loss += l1_loss.item()

                    if phase == 'train':
                        # reset discriminator gradients
                        optimizers['disc'].zero_grad()

                    # train / inference the discriminator
                    with torch.set_grad_enabled(phase == 'train'):
                        prediction_real = self.discriminator(real_img_lab)
                        prediction_fake = self.discriminator(fake_img_lab.detach())

                        loss_real = losses['disc'](prediction_real, target_ones * self.cfg.smoothing)
                        loss_fake = losses['disc'](prediction_fake, target_zeros)
                        full_disc_loss = loss_real + loss_fake

                        if phase == 'train':
                            full_disc_loss.backward()
                            optimizers['disc'].step()

                    epoch_disc_real_loss += loss_real.item()
                    epoch_disc_fake_loss += loss_fake.item()
                    epoch_disc_real_acc += np.mean(prediction_real.detach().cpu().numpy() > 0.5)
                    epoch_disc_fake_acc += np.mean(prediction_fake.detach().cpu().numpy() <= 0.5)

                    # save the first sample for later
                    if phase == 'test' and idx == 0:
                        sample_real_img_lab = real_img_lab
                        sample_fake_img_lab = fake_img_lab

                # display losses
                save_losses(self.cfg , epoch_gen_adv_loss, epoch_gen_l1_loss,
                             epoch_disc_real_loss, epoch_disc_fake_loss,
                             epoch_disc_real_acc, epoch_disc_fake_acc,
                             len(data_loaders[phase]), self.cfg.l1_weight)

                # save after every nth epoch
                if phase == 'test':
                    if epoch % self.cfg.checkpoint_frequency == 0 or epoch == self.cfg.max_epoch - 1:
                        gen_path = os.path.join(self.cfg.output_path, 'checkpoint_ep{}_gen.pt'.format(epoch))
                        disc_path = os.path.join(self.cfg.output_path, 'checkpoint_ep{}_disc.pt'.format(epoch))
                        torch.save(self.generator.state_dict(), gen_path)
                        torch.save(self.discriminator.state_dict(), disc_path)
                        print('Checkpoint.')


    def inference(self,img):
        img_bgr = img.astype(np.float32) / 255.0
        # transform to LAB
        img_lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)
        img_lab[:, :, 0] = img_lab[:, :, 0] / 50 - 1
        img_lab[:, :, 1] = img_lab[:, :, 1] / 127
        img_lab[:, :, 2] = img_lab[:, :, 2] / 127
        img_lab = img_lab.transpose((2, 0, 1))
        out = self.generator(torch.tensor([img_lab[0:1,:,:]]))
        print(img_lab.shape)
        img_temp = F.interpolate(torch.tensor([img_lab[0:1,:,:]]), size=(32,32),mode='bilinear',align_corners=True)
        print(img_temp.shape , out.shape)
        out = torch.cat([img_temp , out], dim=1).detach().cpu().numpy()
        out = out[0].transpose((1, 2, 0))
        out[:, :, 0] = (out[:, :, 0] + 1) * 50
        out[:, :, 1] = out[:, :, 1] * 127
        out[:, :, 2] = out[:, :, 2] * 127
        # transform to bgr
        out = cv2.cvtColor(out, cv2.COLOR_LAB2BGR)
        # to int8
        out = (out * 255.0).astype(np.uint8)

        return out

    def __adjust_lr(self,optimizer, global_step, base_lr, lr_decay_rate=0.1, lr_decay_steps=6e4):
        """Adjust the learning rate of the params of an optimizer."""
        lr = base_lr * (lr_decay_rate ** (global_step/lr_decay_steps))
        if lr < 1e-6:
            lr = 1e-6

        for param_group in optimizer.param_groups:
            param_group['lr'] = lr


# if __name__ == '__main__':
#     import cv2
#     # dataloaders = Cifar10Dataset('cifar10').get_dataloaders()
#     cfg = get_cfg()
#     cfg.initial_weights_generator = 'output/checkpoint_ep99_gen.pt'
#     model = ColourGAN(cfg,inference=True)
#     # model.train(dataloaders['train'],dataloaders['test'])
#     img = cv2.imread('output/airbus_s_000413.png')
#     out = model.inference(img)
#     cv2.imwrite('output/temp2.png', out)

