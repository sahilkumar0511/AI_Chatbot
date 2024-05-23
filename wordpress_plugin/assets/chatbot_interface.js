jQuery(document).ready(function($) {
    $('#chatbot-submit').on('click', function() {
        var userQuery = $('#chatbot-input').val();

        $.ajax({
            type: 'POST',
            url: chatbot_ajax.ajax_url,
            data: {
                action: 'chatbot_query',
                query: userQuery
            },
            success: function(response) {
                $('#chatbot-response').text(response.response);
            },
            error: function() {
                $('#chatbot-response').text('Error contacting the chatbot');
            }
        });
    });
});