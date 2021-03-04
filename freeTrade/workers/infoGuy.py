from alpaca_trade_api import Stream


class InfoGuy(Stream):
    """
    InfoGuy acts as an interface between the user and the alpaca API, it allows for calls
    to get historic data as well as current data. This data is loaded into a dataclass
    that structures what data the user should expect to see from the endpoints.
    This service relies on the variables being set in the running environment, these variables are
    as follows:
    * APCA_API_KEY: public for alpaca api
    * APCA_API_SECRET_KEY: secret key for alpaca api
    * APCA_API_BASE_URL: base uri for making requests to alpaca
    * APCA_API_DATA_URL: base uri for making data requests to alpaca
    """

    def __init__(self, securities):
        """
        Defines the class streaming platform, this class handles streaming a list of changing securities
        Args:
            securities:
        """
        super.__init__()
        self.securities = securities

    async def _stream_security(self, security):
        pass
