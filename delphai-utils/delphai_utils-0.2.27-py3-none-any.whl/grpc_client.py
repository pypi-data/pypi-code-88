from typing import Any, Optional, Sequence, Tuple
from grpc.aio import insecure_channel as async_insecure_channel
from grpc import insecure_channel


def get_grpc_client(Stub, address: str, is_async: bool = True, options: Optional[Sequence[Tuple[str, Any]]] = {}):
  if is_async:
    channel = async_insecure_channel(address, options=options)
  else:
    channel = insecure_channel(address, options=options)
  client = Stub(channel)
  return client