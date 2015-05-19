chatApp.controller('ChatController', [
    '$scope', '$attrs', '$websocket',
    function ($scope, $attrs, $websocket) {
        $scope.chatHistory = [];
        $scope.socket = $websocket.$new($attrs.socketUrl);

        $scope.playerName = "Player " + Math.random();

        $scope.sendMessage = function (message) {
            $scope.socket.$emit('chatRoom', {
                player: $scope.playerName,
                message: message
            });
        };

        $scope.onChatMessageKeyUp = function(e) {
            var isEnterKeyUp = e.keyCode == 13;
            if (isEnterKeyUp) {
                $scope.sendMessage($scope.chatMessage);
                $scope.chatMessage = '';
            }
        };

        $scope.socket.$on('$open', function () {
            $scope.socket.$emit('chatRoom', {
                player: $scope.playerName,
                message: "Joined the room."
            });
        });

        $scope.socket.$on('chatRoom', function (data) {
            console.log($scope.$$phase);
            $scope.chatHistory.push(data);
            $scope.$apply();
        });

        $scope.socket.$on('$close', function () {
            console.log('Socket closed.');
        });
    }
]);
