import os
import time
import torch
import argparse
import deepspeed
import torch.distributed as dist


TRIALS = 5


N = 500000
M = 4000


def timed_allreduce(mat):
    torch.cuda.synchronize()
    pre = time.perf_counter()
    dist.all_reduce(mat)
    torch.cuda.synchronize()
    duration = time.perf_counter() - pre
    tput = ((mat.numel() * 4 * 2) / duration) * 8
    return tput


def run(local_rank):
    global_rank = dist.get_rank()
    if global_rank == 0:
        print(global_rank, "data size:", mat.numel() * 4 / 1e9, "GB")

    mat = torch.rand(N, M, dtype=torch.float32).cuda(local_rank)

    tputs = []
    busbws = []
    for trial in range(TRIALS):
        tput, busbw = timed_allreduce(mat)
        if trial > 2:
            tputs.append(tput)
            busbws.append(busbw)

    local_avg = sum(tputs) / len(tputs)
    local_avg_bb = sum(busbws) / len(busbws)
    t = torch.tensor([local_avg/1e9, local_avg_bb/1e9], device='cuda')
    dist.all_reduce(t)
    tput_avg = t[0] / dist.get_world_size()
    busbw_avg = t[1] / dist.get_world_size()
    if dist.get_rank() == 0:
        print('tput_avg (Gbps):', tput_avg.item())


def init_processes(local_rank, fn, backend='nccl'):
    deepspeed.init_distributed(dist_backend=backend)
    local_rank = int(os.environ['LOCAL_RANK'])
    torch.cuda.set_device(local_rank)
    fn(local_rank)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--local_rank", type=int)
    args = parser.parse_args()
    rank = args.local_rank
    #print("local_rank: %d" % rank)
    init_processes(local_rank=rank, fn=run)