$('#menu').wijmenu();
$('#tree').wijtree();
$('#gallery').wijgallery({
    thumbsDisplay: 3
});
$('#widget-explorer').click(function() {
    $('#dialog').wijdialog({ width: 840, height: 640, contentUrl: 'http://wijmo.com/demo/explore/?showall=true', autoOpen: true});
})
$('body').removeClass('invisible');
if ($('#contact').length) {
    var messageTypes = $.map(["Comment", "Review", "Errata", "Other"], function (type) {
        return {label: type, value: type}
    });
    //Create ViewModel
    var ViewModel = function () {
        this.subject = ko.observable('');
        this.body = ko.observable('');
        this.messageType = ko.observable('Comment');
        this.submit = function () {
            socket.emit('message', ko.toJSON(viewModel));
        }
    };
    $('#subject,#body').wijtextbox();
    $('button').button();

    var viewModel = new ViewModel();
    ko.applyBindings(viewModel);
}