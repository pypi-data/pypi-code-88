import torch
from tqdm import tqdm

from . import utils, attack_steps



STEPS = {
    'inf': attack_steps.LinfStep,
    '2': attack_steps.L2Step,
    'unconstrained': attack_steps.UnconstrainedStep,
    'fourier': attack_steps.FourierStep,
    'random_smooth': attack_steps.RandomStep
}


def PGD(mod, im, targ, normalization, step_size, Nsteps, constraint='inf',
        eps=None, targeted=True, custom_loss=None, random_start=False, use_tqdm=False):
    '''
    Compute adversarial examples for given model.
    Args:
        mod: model
        im (tensor): batch of images
        targ (tensor): batch of labels
        normalization (function): normalization function to be applied on inputs
        step_size (float): optimization step size
        Nsteps (int): number of optimization steps
        eps (float): radius of L2 ball
        targeted (bool): True if we want to maximize loss, else False
        custom_loss (function): custom loss function to employ (optional)
        
    Returns:
        x: batch of adversarial examples for input images
    '''
    assert targ is not None
    prev_training = bool(mod.training)
    mod.eval()

    x = im.detach()
    step_class = STEPS[constraint] if isinstance(constraint, str) else constraint
    step = step_class(eps=eps, orig_input=x, step_size=step_size)

    if random_start:
        x = step.random_perturb(x)
    
    sign = -1 if targeted else 1

    it = iter(range(Nsteps))
    if use_tqdm:
        it = tqdm(iter(range(Nsteps)), total=Nsteps) 

    for i in it:    
        x = x.clone().detach().requires_grad_(True)
        grad, loss = utils.get_gradient(mod, x, targ, normalization, 
                               custom_loss=custom_loss)

        if use_tqdm:
            it.set_description(f'Loss: {loss}')
        
        with torch.no_grad():
            # l = len(x.shape) - 1
            # g_norm = torch.norm(grad.view(grad.shape[0], -1), dim=1).view(-1, *([1]*l))
            # scaled_g = grad / (g_norm + 1e-30)
            # scaled_g[scaled_g > 1.5] = 0
            # g_norm_scaled = torch.norm(scaled_g.view(scaled_g.shape[0], -1), dim=1).view(-1, *([1]*l))
            # print(i, g_norm.view(-1), g_norm_scaled.view(-1), f"targeted: {targeted}")
            
            x = step.step(x, sign * grad)
            x = step.project(x)
    
    if prev_training:
        mod.train()

    return x.detach()