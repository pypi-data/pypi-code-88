"""Functions for running and evaluating models."""
from contextlib import contextmanager
import gc
from typing import Callable, Dict, Iterable, Optional, Tuple, TypeVar, Union
import warnings

import torch
from torch import Tensor
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm

from .utils import Timer, map_structure, get_device


T = TypeVar('T')

# A callback that given (model, inputs, labels) outputs transformed (inputs, labels).
DataTransform = Callable[[nn.Module, Tensor, Tensor], Tuple[Tensor, Tensor]]


def get_predictions(model: nn.Module, inputs: Tensor) -> Tensor:
    with eval_mode(model), torch.no_grad():
        logits = model(tensor_to(inputs, model))
        result = logits.argmax(dim=1)
    return result.to(inputs.device)


def evaluate(
    model: nn.Module,
    data_loader: DataLoader,
    data_transform: Optional[DataTransform] = None,
    timeout: Optional[float] = None,  # float seconds or None
    use_tqdm: bool = True,
    desc: str = "Evaluation"
) -> Dict[str, float]:
    warn_if_not_cuda(model)
    loss = 0
    correct = 0
    total = 0
    criterion = nn.CrossEntropyLoss()
    if timeout is not None:
        timer = Timer()
    progress_bar = tqdm(data_loader, desc=desc, unit="batch", delay=1, disable=not use_tqdm)
    with eval_mode(model), progress_bar:
        for inputs, labels in tensors_to(progress_bar, model):
            if data_transform is not None:
                inputs, labels = data_transform(model, inputs, labels)
            with torch.no_grad():
                outputs = model(inputs)
                loss += criterion(outputs, labels).item() * labels.shape[0]
                predictions = torch.argmax(outputs.data, 1)
                correct += (predictions == labels).sum().item()
                total += labels.shape[0]
            progress_bar.set_postfix(
                refresh=False, loss=loss / total, accuracy=f"{100 * correct / total:.2f}%"
            )
            if timeout is not None and timer.elapsed() > timeout:
                break
    return {"loss": loss / total, "accuracy": 100 * correct / total}


def warn_if_not_cuda(module: nn.Module) -> None:
    for p in module.parameters():
        if not str(p.device).startswith("cuda"):
            warnings.warn("Module not on CUDA.", stacklevel=2)
            break


def tensor_to(
    tensor: torch.Tensor,
    where_to: Union[torch.nn.Module, torch.Tensor, torch.device],
    non_blocking=True,
    copy=False,
):
    """Make tensor compatible with `where_to` (eg. move to the where_to.device).

    In the future this could adjust other things like float precision.
    """
    return tensor.to(get_device(where_to), non_blocking=non_blocking, copy=copy)


def tensors_to(
    tensors: Union[DataLoader, Iterable[torch.Tensor]],
    where_to: Union[torch.nn.Module, torch.Tensor, torch.device],
    non_blocking=True,
    copy=False,
):
    """Make tensors compatible with `where_to` (eg. move to the where_to.device)."""
    for t in tensors:
        if isinstance(t, torch.Tensor):
            yield tensor_to(t, where_to, non_blocking=non_blocking, copy=copy)
        else:
            yield [tensor_to(tt, where_to, non_blocking=non_blocking, copy=copy) for tt in t]


def structure_to(
    structure,
    where_to: Union[torch.nn.Module, torch.Tensor, torch.device],
    non_blocking=True,
    copy=False,
):
    """Make structure compatible with `where_to` (eg. move to the where_to.device)."""
    return map_structure(structure, lambda t: tensor_to(t, where_to) if isinstance(t, torch.Tensor) else t)


def clean(cuda: bool = True) -> None:
    """Clean-up interruped tqdm instances and garbage-collect CUDA cache."""
    getattr(tqdm, "_instances", {}).clear()
    gc.collect()
    if cuda:
        torch.cuda.empty_cache()
    print(end="", flush=True)


@contextmanager
def interruptible():
    """Context manager from which keyboard interrupts exit cleanly.

    Instead of the default backtrace, we catch the exception and just print "KeyboardInterrupt".
    The context also always calls `clean(cuda=False)` on exit.
    """
    try:
        yield
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    finally:
        clean(cuda=False)


@contextmanager
def train_mode(module: nn.Module):
    """Context which turns on training mode, and returns to original mode on exit."""
    was_training = module.training
    module.train()
    try:
        yield
    finally:
        module.train(was_training)


@contextmanager
def eval_mode(module: nn.Module):
    """Context which turns on eval mode, and returns to original mode on exit."""
    was_training = module.training
    module.eval()
    try:
        yield
    finally:
        module.train(was_training)
