"""
    Defines our constants
"""

PROTOCOL_DEFAULT_TIMEOUT = 60
PROTOCOL_DEFAULT_PORT = 5672
PROTOCOL_HEADER = b'AMQP\x01\x01\x00\x09'

# protocol
TYPE_METHOD = 1
TYPE_HEADER = 2
TYPE_BODY = 3
TYPE_HEARTBEAT = 4

FRAME_END = 0xCE

# classes
CLASS_CONNECTION = 10
CLASS_CHANNEL = 20
CLASS_EXCHANGE = 40
CLASS_QUEUE = 50
CLASS_BASIC = 60
CLASS_TX = 90

CONNECTION_START = 10
CONNECTION_START_OK = 11
CONNECTION_SECURE = 20
CONNECTION_SECURE_OK = 21
CONNECTION_TUNE = 30
CONNECTION_TUNE_OK = 31
CONNECTION_OPEN = 40
CONNECTION_OPEN_OK = 41
CONNECTION_CLOSE = 50
CONNECTION_CLOSE_OK = 51

CHANNEL_OPEN = 10
CHANNEL_OPEN_OK = 11
CHANNEL_FLOW = 20
CHANNEL_FLOW_OK = 21
CHANNEL_CLOSE = 40
CHANNEL_CLOSE_OK = 41

EXCHANGE_DECLARE = 10
EXCHANGE_DECLARE_OK = 11
EXCHANGE_DELETE = 20
EXCHANGE_DELETE_OK = 21
EXCHANGE_BIND = 30
EXCHANGE_BIND_OK = 31

QUEUE_DECLARE = 10
QUEUE_DECLARE_OK = 11
QUEUE_BIND = 20
QUEUE_BIND_OK = 21
QUEUE_UNBIND = 50
QUEUE_UNBIND_OK = 51
QUEUE_PURGE = 30
QUEUE_PURGE_OK = 31
QUEUE_DELETE = 40
QUEUE_DELETE_OK = 41

BASIC_QOS = 10
BASIC_QOS_OK = 11
BASIC_CONSUME = 20
BASIC_CONSUME_OK = 21
BASIC_CANCEL = 30
BASIC_CANCEL_OK = 31
BASIC_PUBLISH = 40
BASIC_RETURN = 50
BASIC_DELIVER = 60
BASIC_GET = 70
BASIC_GET_OK = 71
BASIC_GET_EMPTY = 72
BASIC_ACK = 80
BASIC_REJECT = 90
BASIC_RECOVER_ASYNC = 100
BASIC_RECOVER = 110
BASIC_RECOVER_OK = 111

TX_SELECT = 10
TX_SELECT_OK = 11
TX_COMMIT = 20
TX_COMMIT_OK = 21
TX_ROLLBACK = 30
TX_ROLLBACK_OK = 31
