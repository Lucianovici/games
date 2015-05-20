chatApp.controller('ChatController', [
    '$scope', '$attrs', 'websocketService',
    function ($scope, $attrs, websocketService) {
        websocketService.init($attrs.socketUrl);
    }
]);

chatApp.controller('RoomController', [
    '$scope', 'userService', 'websocketService',
    function ($scope, userService, websocketService) {
        $scope.chatHistory = [];

        $scope.sendMessage = function (message) {
            websocketService.socket.$emit('chatRoom', {
                username: userService.username,
                message: message
            });
        };

        $scope.onChatMessageKeyUp = function (e) {
            var isEnterKeyUp = e.keyCode == 13;
            if (isEnterKeyUp) {
                $scope.sendMessage($scope.chatMessage);
                $scope.chatMessage = '';
            }
        };

        $scope.isUsernameSet = function () {
            return !!userService.username;
        };

        websocketService.socket.$on('$open', function () {
        });

        websocketService.socket.$on('chatRoom', function (data) {
            $scope.chatHistory.push(data);
            $scope.$apply();
        });

        websocketService.socket.$on('$close', function () {
            console.log('Socket closed.');
        });
    }
]);

chatApp.controller('UserController', [
    '$scope', 'userService', 'websocketService',
    function ($scope, userService, websocketService) {
        $scope.joinRoomChat = function (username) {
            userService.setUsername(username);
            $scope.sendWelcomeMessage();
        };

        $scope.sendWelcomeMessage = function () {
            websocketService.socket.$emit('chatRoom', {
                username: userService.username,
                message: "Joined the room."
            });
        };

        $scope.onUsernameKeyUp = function (e) {
            var isEnterKeyUp = e.keyCode == 13;
            if (isEnterKeyUp) {
                $scope.joinRoomChat($scope.username);
            }
        };

        $scope.isUsernameSet = function () {
            return !!userService.username;
        };
    }
]);