var ChatManager = {
    init: function () {
        this.$chat = $('#chat');
        this.socketURL = this.$chat.data('socket-url');

        WebSocketManager.init(this.socketURL);
        WebSocketManager.setReceiveHandler(this.receiveMessage.bind(ChatManager));

        this.bindEvents();
    },

    bindEvents: function () {
        this.$chat.find('.chat-send-btn').click(this.onSendBtnClick.bind(ChatManager));
        this.$chat.find('.chat-input-box').keydown(this.onInputBoxKeyDown.bind(ChatManager));
    },

    sendMessage: function () {
        WebSocketManager.sendMessage(this.$chat.find('.chat-input-box').val());
    },

    receiveMessage: function(e) {
        var $msg = $('<p>').html(e.data);
        this.$chat.find('.chat-bilboard').append($msg);
    },

    onSendBtnClick: function (e) {
        this.sendMessage();
    },

    onInputBoxKeyDown: function (e) {
        var isEnterKey = e.keyCode === 13;
        if (isEnterKey) {
            e.preventDefault();
            this.sendMessage();
            this.$chat.find('.chat-input-box').val('');  //clear its value.
        }
    }
};

(function ($) {
    ChatManager.init();
})(jQuery);