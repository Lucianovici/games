chatApp.factory('websocketService', ['$websocket', function ($websocket) {
    return {
        init: function (socketUrl) {
            this.socketUrl = socketUrl;
            this.socket = $websocket.$new(this.socketUrl);
        }
    }
}]);
chatApp.factory('userService', function () {
    return {
        username: '',
        setUsername: function (username) {
            this.username = username;
        }
    }
});