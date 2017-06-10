
var requestState, Requests = {
    state: {},

    resetGame: function() {
        thisState = this.state;
        this.putRequest('/reset_game/' + game["pk"], function (response) {
            game = JSON.parse(response["currentGame"]);
            activePlayer = JSON.parse(response["activePlayer"]);
            thisState.updateState(activePlayer, game);
        });
    },

    pollState: function(pk){
        thisState = this.state;
        this.getRequest('/game_details/' + pk, function (response) {
            game = JSON.parse(response["currentGame"]);
            activePlayer = JSON.parse(response["activePlayer"]);
            thisState.updateState(activePlayer, game);
        });
    },

    postTurn: function(rowClicked, colClicked) {
        thisState = this.state;
        var data = { "game_id": game["pk"], "active_player_num": game["active_player_num"], "row_clicked": rowClicked, "col_clicked": colClicked }
        this.postRequest('/post_turn/', data, function (response) {
            game = JSON.parse(response["currentGame"]);
            activePlayer = JSON.parse(response["activePlayer"]);
            thisState.updateState(activePlayer, game);
        });
    },

    putRequest: function(serviceUrl, callback = null) {
        var csrftoken = this.getCookie('csrftoken');
        $.ajax({
            url: serviceUrl,
            type: 'PUT',
            headers: { "X-CSRFToken": csrftoken },
            success: function (result) {
                if (callback != null) {
                    callback(result);
                }
            },
            error: function (result) {
                console.log('error');
            }
        });
    },

    postRequest: function(serviceUrl, data, callback = null) {
        var csrftoken = this.getCookie('csrftoken');
        $.ajax({
            url: serviceUrl,
            type: 'POST',
            headers: { "X-CSRFToken": csrftoken },
            data: data,
            success: function (result) {
                if (callback != null) {
                    callback(result);
                }
            },
            error: function (result) {
                console.log('error');
            }
        });
    },

    getRequest: function(serviceUrl, callback = null) {
        var csrftoken = this.getCookie('csrftoken');
        $.ajax({
            url: serviceUrl,
            headers: { "X-CSRFToken": csrftoken },
            type: 'GET',
            success: function (result) {
                if (callback != null) {
                    callback(result);
                }
            },
            error: function (result) {
                console.log('error');
                console.log(result);
            }
        });
    },

    getCookie: function(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    },

    init: function() {
        requestState = this.state;
    },

    instance: function() {
        return this;
    }

};