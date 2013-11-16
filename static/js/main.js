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
    $('textarea,input').wijtextbox();
    $('button').button();
}
setTimeout(function(){
    $('.hidden').removeClass('hidden');
}, 2000)