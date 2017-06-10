var Pieces = {

    settings: {},

    canvas: {},

    init: function() {

    },

    drawCircle: function(col, row, sectionWidth) {
        centerX = col * sectionWidth + sectionWidth / 2;
        centerY = row * sectionWidth + sectionWidth / 2;
        radius = (sectionWidth - 20) / 2
        color = "rgba(255,255,255,0.5"
        lineWidth = 20;
        var context = canvas.getContext('2d');
        context.beginPath();
        context.arc(centerX, centerY, radius, 0, 2 * Math.PI, false);
        context.fillStyle = color;
        context.fill();
        context.lineWidth = lineWidth;
        context.strokeStyle = '#003300';
        context.stroke();
    },

    drawX: function(col, row, sectionWidth) {
        startX = col * sectionWidth + 10;
        startY = row * sectionWidth + 10;
        endX = (col + 1) * sectionWidth - 10;
        endY = (row + 1) * sectionWidth - 10;
        color = "rgba(255,255,255,0.5";
        lineWidth = 20;
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

    instance: function() {
        return this;
    }
};