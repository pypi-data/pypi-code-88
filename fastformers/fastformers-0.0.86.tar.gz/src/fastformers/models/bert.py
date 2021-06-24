import torch

from ..modules import TransformerEncoder, MaskEmbeddings


class BertModel(torch.nn.Module):
    def __init__(
            self, vocab_size: int, dim: int, padding_idx: int,
            max_position_embeddings: int, ffn_size: int, n_heads: int, n_layers: int):
        super().__init__()

        self.embeddings = MaskEmbeddings(
            vocab_size=vocab_size, dim=dim, padding_idx=padding_idx,
            max_position_embeddings=max_position_embeddings
        )
        self.encoder = TransformerEncoder(
            n_heads=n_heads, embedding_size=dim, ffn_size=ffn_size, n_layers=n_layers)

    def forward(self, input_ids: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
        embedding_output = self.embeddings(input_ids=input_ids)
        return self.encoder.forward(embedding_output, attention_mask.to(torch.bool))
