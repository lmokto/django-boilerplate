$(document).ready(function() {
    // Cerrar alerts de bootstrap
    $(".close").click(function(){
        $(".alert").hide();
    });

    // UItoTop-jQuery-Plugin
    $().UItoTop({ easingType: 'easeOutQuart' });
});
