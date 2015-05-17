var WebSocketManager = {
    init: function (url) {
        this.websocket = new WebSocket(url);
        this.websocket.onopen = this.onOpen;
        this.websocket.onmessage = this.onMessage;
        this.websocket.onerror = this.onError;
        this.websocket.onclose = this.onClose;
    },
    setReceiveHandler: function (handler) {
        this.websocket.onmessage = handler;
    },
    onOpen: function (e) {
        console.log("WebSocket connected!");
    },
    onMessage: function (e) {
        console.log("Received:" + e.data);
    },
    onError: function (e) {
        console.error(e);
    },
    onClose: function (e) {
        console.log("WebSocket connection closed");
    },
    sendMessage: function (msg) {
        this.websocket.send(msg);
    }
};