import matplotlib
import os, sys
from os.path import dirname, abspath, join
TEST_DIR = dirname(__file__)
sys.path.insert(0, abspath(join(TEST_DIR, "../")))
from vlkit.lrscheduler import CosineScheduler, MultiStepScheduler
matplotlib.use("Agg")
import matplotlib.pyplot as plt

savedir = join(dirname(__file__), "../data/test")
os.makedirs(savedir, exist_ok=True)

fig, axes = plt.subplots(1, 2, figsize=(12, 3))
for ax in axes:
    ax.grid(alpha=0.5, linestyle='dotted', linewidth=2, color='black')

epochs = 20
loader_len = 10
warmup_epochs = 5

lr_scheduler = CosineScheduler(epoch_size=loader_len, epochs=epochs, repeats=3, repeat_decay=0.8,
        max_lr=0.1, min_lr=0.01, warmup_epochs=warmup_epochs, warmup_init_lr=0.05, noice_std=0.05)

lr_record = []
for i in range(epochs*loader_len):
    lr_record.append(lr_scheduler.step())

axes[0].plot(lr_record, color="blue", linewidth=1)
axes[0].set_xlabel("Iter", fontsize=12)
axes[0].set_ylabel("Learning Rate", fontsize=12)
axes[0].set_title("Cosine Annealing + Restarts + Noice")

# multi step lr
lr_scheduler = MultiStepScheduler(epoch_size=loader_len, epochs=epochs, milestones=[10, 15],
        base_lr=0.1, gamma=[0.1, 0.1], warmup_epochs=warmup_epochs, warmup_init_lr=0.05, noice_std=0.05)
lr_record = []
for i in range(epochs*loader_len):
    lr_record.append(lr_scheduler.step())
axes[1].plot(lr_record, color="blue", linewidth=1)
axes[1].set_xlabel("Iter", fontsize=12)
axes[1].set_ylabel("Learning Rate", fontsize=12)
axes[1].set_title("Warmup + Multistep LR + Noice")

plt.tight_layout()
plt.savefig(join(savedir, "lr_scheduler.svg"))
