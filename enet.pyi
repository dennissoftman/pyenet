"""
This type stub file was generated by cyright.
"""

PACKET_FLAG_RELIABLE = ...
PACKET_FLAG_UNSEQUENCED = ...
PACKET_FLAG_NO_ALLOCATE = ...
PACKET_FLAG_UNRELIABLE_FRAGMENT = ...
EVENT_TYPE_NONE = ...
EVENT_TYPE_CONNECT = ...
EVENT_TYPE_DISCONNECT = ...
EVENT_TYPE_RECEIVE = ...
PEER_STATE_DISCONNECTED = ...
PEER_STATE_CONNECTING = ...
PEER_STATE_ACKNOWLEDGING_CONNECT = ...
PEER_STATE_CONNECTION_PENDING = ...
PEER_STATE_CONNECTION_SUCCEEDED = ...
PEER_STATE_CONNECTED = ...
PEER_STATE_DISCONNECT_LATER = ...
PEER_STATE_DISCONNECTING = ...
PEER_STATE_ACKNOWLEDGING_DISCONNECT = ...
PEER_STATE_ZOMBIE = ...
ENET_CRC32 = ...
class Address:
    ...


class Socket:
    """
    Socket (int socket)

    DESCRIPTION

        An ENet socket.

        Can be used with select and poll.
    """
    def send(self, address: Address, data): # -> int:
        ...
    
    def fileno(self): # -> int:
        ...
    


class Address:
    """
    Address (str address, int port)

    ATTRIBUTES

        str host    Hostname referred to by the Address.
        int port    Port referred to by the Address.

    DESCRIPTION

        An ENet address and port pair.

        When instantiated, performs a resolution upon 'address'. However, if
        'address' is None, enet.HOST_ANY is assumed.
    """
    def __init__(self, host, port) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __richcmp__(self, obj, op): # -> bool:
        ...
    
    @property
    def host(self): # -> unicode | None:
        ...
    
    @host.setter
    def host(self, value): # -> unicode | None:
        ...
    
    @property
    def hostname(self): # -> unicode | None:
        ...
    
    @property
    def port(self): # -> enet_uint16:
        ...
    
    @port.setter
    def port(self, value): # -> enet_uint16:
        ...
    


class Packet:
    """
    Packet (str dataContents, int flags)

    ATTRIBUTES

        str data        Contains the data for the packet.
        int flags       Flags modifying delivery of the Packet:

            enet.PACKET_FLAG_RELIABLE Packet must be received by the target peer
                                      and resend attempts should be made until
                                      the packet is delivered.

            enet.PACKET_FLAG_UNSEQUENCED Packet will not be sequenced with other
                                         packets not supported for reliable
                                         packets.

            enet.PACKET_FLAG_NO_ALLOCATE Packet will not allocate data and user
                                         must supply it instead.

            enet.PACKET_FLAG_UNRELIABLE_FRAGMENT Packet will be fragmented using
                                                 unreliable (instead of reliable)
                                                 sends if it exceeds the MTU...

    DESCRIPTION

        An ENet data packet that may be sent to or received from a peer.

    """
    def __init__(self, data=..., flags=...) -> None:
        ...
    
    def is_valid(self): # -> bool:
        ...
    
    @property
    def data(self): # -> char:
        ...
    
    @property
    def dataLength(self): # -> unsigned int:
        ...
    
    @property
    def flags(self): # -> unsigned short:
        ...
    
    @property
    def sent(self):
        ...
    
    @sent.setter
    def sent(self, value):
        ...
    


class Peer:
    """
    Peer ()

    ATTRIBUTES

        Address address
        int     state       The peer's current state which is one of
                            enet.PEER_STATE_*
        int     packetLoss  Mean packet loss of reliable packets as a ratio with
                            respect to the constant enet.PEER_PACKET_LOSS_SCALE.
        int     packetThrottleAcceleration
        int     packetThrottleDeceleration
        int     packetThrottleInterval
        int     roundTripTime Mean round trip time (RTT), in milliseconds,
                              between sending a reliable packet and receiving
                              its acknowledgement.
        int     incomingPeerID

    DESCRIPTION

        An ENet peer which data packets may be sent or received from.

        This class should never be instantiated directly, but rather via
        enet.Host.connect or enet.Event.Peer.  If you try to access any members
        of a Peer without being properly instantiated from a Host or Event
        object then a MemoryError will be raised.

    """
    def __richcmp__(self, obj, op): # -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def send(self, channelID, packet: Packet): # -> int | None:
        """
        send (int channelID, Packet packet)

        Queues a packet to be sent.

        returns 0 on success, < 0 on failure
        """
        ...
    
    def receive(self, channelID: int): # -> Packet | None:
        """
        receive (int channelID)

        Attempts to dequeue any incoming queued packet.
        """
        ...
    
    def reset(self): # -> None:
        """
        reset ()

        Forcefully disconnects a peer.
        """
        ...
    
    def ping(self): # -> None:
        """
        ping ()

        Sends a ping request to a peer.
        """
        ...
    
    def disconnect(self, data=...): # -> None:
        """
        disconnect ()

        Request a disconnection from a peer.
        """
        ...
    
    def disconnect_later(self, data=...): # -> None:
        """
        disconnect_later ()

        Request a disconnection from a peer, but only after all queued outgoing
        packets are sent.
        """
        ...
    
    def disconnect_now(self, data=...): # -> None:
        """
        disconnect_now ()

        Force an immediate disconnection from a peer.
        """
        ...
    
    def check_valid(self): # -> Literal[True]:
        """
        check_valid ()

        Returns True if there is a valid enet_peer set
        Raises a Memory error if not

        """
        ...
    
    @property
    def host(self): # -> Host | None:
        ...
    
    @property
    def outgoingPeerID(self): # -> enet_uint16 | None:
        ...
    
    @property
    def incomingPeerID(self): # -> enet_uint16 | None:
        ...
    
    @property
    def connectID(self): # -> enet_uint32 | None:
        ...
    
    @property
    def outgoingSessionID(self): # -> enet_uint8 | None:
        ...
    
    @property
    def incomingSessionID(self): # -> enet_uint8 | None:
        ...
    
    @property
    def address(self): # -> Address | None:
        ...
    
    @property
    def data(self): # -> enet_uint32 | None:
        ...
    
    @data.setter
    def data(self, value): # -> enet_uint32 | None:
        ...
    
    @property
    def state(self): # -> ENetPeerState | None:
        ...
    
    @property
    def channelCount(self): # -> size_t | None:
        ...
    
    @property
    def incomingBandwidth(self): # -> enet_uint32 | None:
        ...
    
    @property
    def outgoingBandwidth(self): # -> enet_uint32 | None:
        ...
    
    @property
    def incomingBandwidthThrottleEpoch(self): # -> enet_uint32 | None:
        ...
    
    @property
    def outgoingBandwidthThrottleEpoch(self): # -> enet_uint32 | None:
        ...
    
    @property
    def incomingDataTotal(self): # -> enet_uint32 | None:
        ...
    
    @property
    def outgoingDataTotal(self): # -> enet_uint32 | None:
        ...
    
    @property
    def lastSendTime(self): # -> enet_uint32 | None:
        ...
    
    @property
    def lastReceiveTime(self): # -> enet_uint32 | None:
        ...
    
    @property
    def nextTimeout(self): # -> enet_uint32 | None:
        ...
    
    @property
    def earliestTimeout(self): # -> enet_uint32 | None:
        ...
    
    @property
    def packetLossEpoch(self): # -> enet_uint32 | None:
        ...
    
    @property
    def packetsSent(self): # -> enet_uint32 | None:
        ...
    
    @property
    def packetsLost(self): # -> enet_uint32 | None:
        ...
    
    @property
    def packetLoss(self): # -> enet_uint32 | None:
        ...
    
    @property
    def packetLossVariance(self): # -> enet_uint32 | None:
        ...
    
    @property
    def packetThrottle(self): # -> enet_uint32 | None:
        ...
    
    @property
    def packetThrottleLimit(self): # -> enet_uint32 | None:
        ...
    
    @property
    def packetThrottleCounter(self): # -> enet_uint32 | None:
        ...
    
    @property
    def packetThrottleEpoch(self): # -> enet_uint32 | None:
        ...
    
    @property
    def packetThrottleAcceleration(self): # -> enet_uint32 | None:
        ...
    
    @packetThrottleAcceleration.setter
    def packetThrottleAcceleration(self, value): # -> enet_uint32 | None:
        ...
    
    @property
    def packetThrottleDeceleration(self): # -> enet_uint32 | None:
        ...
    
    @packetThrottleDeceleration.setter
    def packetThrottleDeceleration(self, value): # -> enet_uint32 | None:
        ...
    
    @property
    def packetThrottleInterval(self): # -> enet_uint32 | None:
        ...
    
    @packetThrottleInterval.setter
    def packetThrottleInterval(self, value): # -> enet_uint32 | None:
        ...
    
    @property
    def lastRoundTripTime(self): # -> enet_uint32 | None:
        ...
    
    @property
    def lowestRoundTripTime(self): # -> enet_uint32 | None:
        ...
    
    @property
    def lastRoundTripTimeVariance(self): # -> enet_uint32 | None:
        ...
    
    @property
    def highestRoundTripTimeVariance(self): # -> enet_uint32 | None:
        ...
    
    @property
    def roundTripTime(self): # -> enet_uint32 | None:
        ...
    
    @property
    def roundTripTimeVariance(self): # -> enet_uint32 | None:
        ...
    
    @property
    def mtu(self): # -> enet_uint32 | None:
        ...
    
    @property
    def windowSize(self): # -> enet_uint32 | None:
        ...
    
    @property
    def reliableDataInTransit(self): # -> enet_uint32 | None:
        ...
    
    @property
    def outgoingReliableSequenceNumber(self): # -> enet_uint16 | None:
        ...
    
    @property
    def flags(self): # -> enet_uint16 | None:
        ...
    
    @property
    def incomingUnsequencedGroup(self): # -> enet_uint16 | None:
        ...
    
    @property
    def outgoingUnsequencedGroup(self): # -> enet_uint16 | None:
        ...
    
    @property
    def eventData(self): # -> enet_uint32 | None:
        ...
    


class Event:
    """
    Event ()

    ATTRIBUTES

        int     type        Type of the event.  Will be enet.EVENT_TYPE_*.
        Peer    peer        Peer that generated the event.
        int     channelID
        Packet  packet

    DESCRIPTION

        An ENet event as returned by enet.Host.service.

        This class should never be instantiated directly.
    """
    def __init__(self) -> None:
        ...
    
    @property
    def type(self): # -> ENetEventType:
        ...
    
    @property
    def peer(self): # -> Peer:
        ...
    
    @property
    def channelID(self): # -> unsigned char:
        ...
    
    @property
    def data(self): # -> unsigned int:
        ...
    
    @property
    def packet(self): # -> Packet:
        ...
    


host_static_instances = ...
class Host:
    """
    Host (Address address, int peerCount, int channelLimit,
        int incomingBandwidth, int outgoingBandwidth)

    ATTRIBUTES

        Address address             Internet address of the host.
        Socket  socket              The socket the host services.
        int     incomingBandwidth   Downstream bandwidth of the host.
        int     outgoingBandwidth   Upstream bandwidth of the host.

    DESCRIPTION

        An ENet host for communicating with peers.

        If 'address' is None, then the Host will be client only.
    """
    def __init__(self, address: Address = ..., peerCount=..., channelLimit=..., incomingBandwidth=..., outgoingBandwidth=...) -> None:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def connect(self, address: Address, channelCount, data=...): # -> Peer | None:
        """
        Peer connect (Address address, int channelCount, int data)

        Initiates a connection to a foreign host and returns a Peer.
        """
        ...
    
    def check_events(self): # -> Event | None:
        """
        Checks for any queued events on the host and dispatches one if available
        """
        ...
    
    def service(self, timeout, fast_drop=...): # -> Event | None:
        """
        Event service (int timeout)

        Waits for events on the host specified and shuttles packets between
        the host and its peers. The timeout is in milliseconds.

        if fast_drop is set, None can be returned instead
        """
        ...
    
    def flush(self): # -> None:
        """
        flush ()

        Sends any queued packets on the host specified to its designated peers.
        """
        ...
    
    def broadcast(self, channelID, packet: Packet): # -> None:
        """
        broadcast (int channelID, Packet packet)

        Queues a packet to be sent to all peers associated with the host.
        """
        ...
    
    def compress_with_range_coder(self): # -> int | None:
        """
        Sets the packet compressor the host should use to the default range coder
        """
        ...
    
    @property
    def socket(self): # -> Socket:
        ...
    
    @property
    def address(self): # -> Address | None:
        ...
    
    @property
    def incomingBandwidth(self): # -> enet_uint32:
        ...
    
    @incomingBandwidth.setter
    def incomingBandwidth(self, value): # -> enet_uint32:
        ...
    
    @property
    def outgoingBandwidth(self): # -> enet_uint32:
        ...
    
    @outgoingBandwidth.setter
    def outgoingBandwidth(self, value): # -> enet_uint32:
        ...
    
    @property
    def peers(self): # -> list:
        ...
    
    @property
    def peerCount(self): # -> size_t:
        ...
    
    @property
    def channelLimit(self): # -> unsigned int:
        ...
    
    @channelLimit.setter
    def channelLimit(self, value): # -> unsigned int:
        ...
    
    @property
    def totalSentData(self): # -> unsigned int:
        ...
    
    @totalSentData.setter
    def totalSentData(self, value): # -> unsigned int:
        ...
    
    @property
    def totalSentPackets(self): # -> unsigned int:
        ...
    
    @totalSentPackets.setter
    def totalSentPackets(self, value): # -> unsigned int:
        ...
    
    @property
    def totalReceivedData(self): # -> unsigned int:
        ...
    
    @totalReceivedData.setter
    def totalReceivedData(self, value): # -> unsigned int:
        ...
    
    @property
    def totalReceivedPackets(self): # -> unsigned int:
        ...
    
    @totalReceivedPackets.setter
    def totalReceivedPackets(self, value): # -> unsigned int:
        ...
    
    @property
    def intercept(self): # -> object:
        ...
    
    @intercept.setter
    def intercept(self, value): # -> object:
        ...
    
    @property
    def checksum(self): # -> int:
        ...
    
    @checksum.setter
    def checksum(self, value): # -> int:
        ...

