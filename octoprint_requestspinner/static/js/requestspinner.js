$(function() {
    var requestSpinner = $("#requestspinner");
    if (requestSpinner.length > 0) {
        $(document).ajaxStart(function() {
            log.debug("Requests started...");
            requestSpinner.show("slow");
        });
        $(document).ajaxStop(function() {
            log.debug("Requests done");
            requestSpinner.hide("slow");
        });
    }
});
