from typing import Optional, Tuple

import torch
from torch.nn import Module

from .base_modules import Linear


class MultiHeadAttention(Module):
    def __init__(self, n_heads: int, dim: int):
        super().__init__()
        self.pre_attention = Linear(dim, dim * 3)
        self.out_lin = Linear(dim, dim)

        self.n_heads = n_heads
        self.dim_per_head = dim // n_heads

    def forward(
            self,
            hidden_states,
            mask: torch.Tensor,
            incr_state: Optional[torch.Tensor] = None, get_incr_state: bool = False
    ) -> Tuple[torch.Tensor, Optional[torch.Tensor]]:
        batch_size, seq_len = hidden_states.shape[:2]

        pre_attn = self.pre_attention(hidden_states)
        pre_attn = pre_attn.view(batch_size, seq_len, 3, self.n_heads, self.dim_per_head).transpose(1, 3)
        query = pre_attn[:, :, 0]
        k_v = pre_attn[:, :, 1:]

        if incr_state is not None:
            k_v = torch.cat([incr_state, k_v], dim=3)

        dot_prod = torch.matmul(query, k_v[:, :, 0].transpose(2, 3))

        dot_prod += mask

        attn_weights = dot_prod.softmax(dim=-1)

        context_layer = torch.matmul(attn_weights, k_v[:, :, 1])
        context_layer = context_layer.transpose(1, 2).flatten(2, 3)

        context_layer = self.out_lin(context_layer)

        return context_layer, k_v if get_incr_state else None


class DecoderEncoderAttention(Module):
    def __init__(self, n_heads: int, dim: int):
        super().__init__()
        self.q_lin = Linear(dim, dim)
        self.out_lin = Linear(dim, dim)

        self.n_heads = n_heads
        self.dim_per_head = dim // n_heads

    def forward(self, query: torch.Tensor, mask: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        batch_size, seq_len, dim = query.shape

        query = self.q_lin(query)
        query = query.view(batch_size, seq_len, self.n_heads, self.dim_per_head).transpose(1, 2)

        dot_prod = torch.matmul(query, key.transpose(2, 3))

        dot_prod += mask

        attn_weights = dot_prod.softmax(dim=-1)

        context_layer = torch.matmul(attn_weights, value)
        context_layer = context_layer.transpose(1, 2).flatten(2, 3)

        return self.out_lin(context_layer)
