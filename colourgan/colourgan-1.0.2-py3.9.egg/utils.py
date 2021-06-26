'''Utility Functions for Model.'''
import os

def save_losses(cfg , epoch_gen_adv_loss, epoch_gen_l1_loss, epoch_disc_real_loss, epoch_disc_fake_loss,
                 epoch_disc_real_acc, epoch_disc_fake_acc, data_loader_len, l1_weight):
    """Create a display all the losses and accuracies."""
    if os.path.exists(os.path.join(cfg.output_path , cfg.training_stats_file)):
        with open(os.path.join(cfg.output_path , cfg.training_stats_file) , 'r') as f:
            data = f.read()
    else:
        data = ''

    log1 = '  Generator: adversarial loss = {:.4f}, L1 loss = {:.4f}, full loss = {:.4f}'.format(
        epoch_gen_adv_loss / data_loader_len,
        epoch_gen_l1_loss / data_loader_len,
        (epoch_gen_adv_loss / data_loader_len)*(1.0-l1_weight) + (epoch_gen_l1_loss / data_loader_len)*l1_weight
    )

    log2 = '  Discriminator: loss = {:.4f}'.format(
        (epoch_disc_real_loss + epoch_disc_fake_loss) / (data_loader_len*2)
    )

    log3 = '                 acc. = {:.4f} (real acc. = {:.4f}, fake acc. = {:.4f})'.format(
        (epoch_disc_real_acc + epoch_disc_fake_acc) / (data_loader_len*2),
        epoch_disc_real_acc / data_loader_len,
        epoch_disc_fake_acc / data_loader_len
    )
    with open(os.path.join(cfg.output_path , cfg.training_stats_file) , 'w') as f:
        f.write(data + '\n' + log1 + '\n' + log2 + '\n' + log3)

