var gameSettings, gameState, gameEvents, GameBoard = {

    settings: {
        boardContainer: {}
    },

    events: {
        stateChanged: {},
        callStateChanged: function() {
            if (this.stateChanged != undefined) {
                this.stateChanged();
            }
        },

        canvasClicked: {},
        callCanvasClicked: function(e) {
            if (this.canvasClicked != undefined) {
                this.canvasClicked(e);
            }
        }
    },

    canvas: {},

    state: {
        activePlayer: {},
        game: {},
        updateState: function(newActivePlayer, newGame) {
            this.activePlayer = newActivePlayer;
            this.game = newGame;
            gameEvents.callStateChanged();
        }
    },

    init: function(boardContainer, canvasClickedEventHandler, stateChangedEventHandler) {
        //this combined with the declaration of s above ensures that all modules have access to settings
        gameSettings = this.settings;
        gameState = this.state;
        gameEvents = this.events;

        this.settings.boardContainer = boardContainer;
        this.events.canvasClicked = canvasClickedEventHandler;
        this.events.stateChanged = stateChangedEventHandler;

        this.canvas = document.createElement("canvas");
        this.canvas.width = this.settings.boardContainer.clientWidth;
        this.canvas.height = this.settings.boardContainer.clientHeight;
        this.context = this.canvas.getContext("2d");
        this.settings.boardContainer.append(this.canvas);
        thisEvents = this.events
        this.canvas.addEventListener('click', function(e) {
            thisEvents.callCanvasClicked(e);
        }, false);
    },

    instance: function() {
        return this;
    },

    draw_board: function() {
        this.canvas.width = this.settings.boardContainer.clientWidth;
        this.canvas.height = this.settings.boardContainer.clientHeight;
        var sectionWidth = this.settings.boardContainer.clientWidth / 3;
        this.clear();
        s = new component(this.context, this.settings.boardContainer.clientWidth, 10, "black", 0, sectionWidth - 5);
        s.update();
        s = new component(this.context, this.settings.boardContainer.clientWidth, 10, "black", 0, 2 * sectionWidth - 5);
        s.update();
        s = new component(this.context, 10, this.settings.boardContainer.clientWidth, "black", sectionWidth - 5, 0);
        s.update();
        s = new component(this.context, 10, this.settings.boardContainer.clientWidth, "black", 2 * sectionWidth - 5, 0);
        s.update();
    },
    drawX: function(col, row, sectionWidth) {
        startX = col * sectionWidth + 10;
        startY = row * sectionWidth + 10;
        endX = (col + 1) * sectionWidth - 10;
        endY = (row + 1) * sectionWidth - 10;
        color = "rgba(255,255,255,0.5";
        lineWidth = 20;
        var canvas = $("canvas")["0"];
        var context = canvas.getContext('2d');
        context.beginPath();
        context.moveTo(startX, startY);
        context.lineTo(endX, endY);
        context.fillStyle = 'black';
        context.fill();
        context.lineWidth = lineWidth;
        context.strokeStyle = '#003300';
        context.stroke();
        context.beginPath();
        context.moveTo(endX, startY);
        context.lineTo(startX, endY);
        context.fillStyle = 'black';
        context.fill();
        context.lineWidth = lineWidth;
        context.strokeStyle = '#003300';
        context.stroke();
    },
    drawCircle: function(col, row, sectionWidth) {
        centerX = col * sectionWidth + sectionWidth / 2;
        centerY = row * sectionWidth + sectionWidth / 2;
        radius = (sectionWidth - 20) / 2
        color = "rgba(255,255,255,0.5"
        lineWidth = 20;
        var canvas = $("canvas")["0"];
        var context = canvas.getContext('2d');
        context.beginPath();
        context.arc(centerX, centerY, radius, 0, 2 * Math.PI, false);
        context.fillStyle = color;
        context.fill();
        context.lineWidth = lineWidth;
        context.strokeStyle = '#003300';
        context.stroke();
    },

    clear: function() {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    },

    updateGameArea: function() {
        $('#activePlayer').text(activePlayer["name"]);
        myGameArea.clear();
        myGameArea.draw_board();
        for (var i = 0, len = game['state_sequence'].length; i < len; i++) {
            pieceChar = game['state_sequence'][i];
            var sectionWidth = $(".gameBoard")["0"].clientWidth / 3;
            switch (pieceChar) {
                case 'X':
                    drawX(i % 3, Math.floor(i / 3), sectionWidth);
                    break;
                case 'O':
                    drawCircle(i % 3, Math.floor(i / 3), sectionWidth);
                    break;
                default:
                    break;
            }
        }
    }


};

function component(context, width, height, color, x, y) {

    this.width = width;
    this.height = height;
    this.x = x;
    this.y = y;
    this.right = x + width;
    this.bottom = y + height;
    this.color = color;
    this.has_changed = false;

    this.update = function() {
        ctx = context;
        ctx.fillStyle = this.color;
        ctx.fillRect(this.x, this.y, this.width, this.height);
    }
}