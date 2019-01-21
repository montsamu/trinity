import rlp

from eth2.beacon.sedes import (
    uint64,
)

from .eth1_data import Eth1Data


class Eth1DataVote(rlp.Serializable):
    """
    Note: using RLP until we have standardized serialization format.
    """
    fields = [
        # Data being voted for
        ('eth1_data', Eth1Data),
        # Vote count
        ('vote_count', uint64),
    ]

    def __init__(self,
                 eth1_data: Eth1Data,
                 vote_count: int) -> None:
        super().__init__(
            eth1_data=eth1_data,
            vote_count=vote_count,
        )
